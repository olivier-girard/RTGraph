#!/usr/bin/python3
import multiprocessing
import sys
import time
import platform
import itertools
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import math
import random as rand
import yaml

import logging as log
import logging.handlers
import argparse

from LiveWindow import *
from CommandWindow import *
from SavedWindow import *

from acqprocessing import AcqProcessing
from ringbuffer2d import RingBuffer2D

from fit_track import *


class Classify(object):   
# object qui renvoie un dictionnaire trié
# Il possede une fonction de trie 
#            une fonction donnant l'energie depose'
#            une fonction donnant le nombre de sensors ayant recu du signal
#......

    def __init__(self,cmd,sensorpath,setuppath):    #cmd = dico Live (Class_EventLive) or dico Saved  (Class_EventSaved)  #data = Tableau 2D
        self.acq_proc=AcqProcessing()
        self.cmd=cmd # dico 
        self.sensors_path=sensorpath
        self.setup_path=setuppath
        self.key="live"
        self.event=[[],[],[],[],[]]     #[eventAll,eventMuon,eventElectron,eventDisintegration,eventHighEnergyElectron]
        self.energie=[[],[],[],[],[]]   
        #self.fit_results = []
        self.securite_random=0
        self.classification_para = {}
        self.configure()
        self.i=0
        self.last_event_type = ""
        self.fit_results = empty_dict = dict.fromkeys(['reg_y','reg_z','m','theta','chi2'])

    def configure(self):
        data = np.genfromtxt(self.sensors_path, dtype=np.float)
        self.acq_proc.load_general_setup_file(self.setup_path)
        self.acq_proc.set_sensor_pos(data[:,5], data[:,4], data[:,0], data[:,1])
        self.x_para = { "min":min(self.acq_proc.x_coords) , "max":max(self.acq_proc.x_coords) , "pitch":(np.unique(self.acq_proc.x_coords)[1] - np.unique(self.acq_proc.x_coords)[0]) }
        self.y_para = { "min":min(self.acq_proc.y_coords) , "max":max(self.acq_proc.y_coords) , "pitch":(np.unique(self.acq_proc.y_coords)[1] - np.unique(self.acq_proc.y_coords)[0]) }
        self.parameters()
    
    def change_mode(self):
        if(self.key=="live"):
            self.cmd=self.acq_proc.Class_EventLive
        if(self.key=="saved"):
            self.cmd=self.acq_proc.Class_EventSaved

    def signal_per_stage(self,data):
        # donne le nombre de signal par etage 
        # et la quantité d'energie deposé pour chaque étage 
        Mip_per_Stage=0
        Signal_per_Stage=0
        Nbr_Signal_per_Stage=[] 
        Nbr_Mip_per_Stage=[]  
        for j, i in enumerate(self.acq_proc.y_coords):
            if(i!=self.acq_proc.y_coords[0]):
                self.Sensor_per_Stage=j
                break
        for j, i in enumerate(data[0:len(self.acq_proc.y_coords)]):
            if(i>0):
                Signal_per_Stage+=1 ## signal counter
                Mip_per_Stage=Mip_per_Stage+i
            if((j+1)%self.Sensor_per_Stage==0):    
                Nbr_Signal_per_Stage.append(Signal_per_Stage)
                Nbr_Mip_per_Stage.append(Mip_per_Stage)
                Signal_per_Stage=0
                Mip_per_Stage=0
        return Nbr_Signal_per_Stage, Nbr_Mip_per_Stage
    
    def isMuon(self, data, Nsig_per_plane, mip_per_plane):
        # Muons - we want:
        # 1) small energy deposit: typically below 30 MIPs in total and below 10 MIPs per layer
        # 2) at least a certain number of layers detecting: let's say 5
        # 3) no more than two hits per stage
        # 4) a fit chi^2 small <-- so we need to perform a fit before classifying
        
        energy_tot=sum(mip_per_plane)  # total energy deposit
        small_Edeposit_per_stage = all(E <= self.classification_para['Muon']['EnergyDepositPerPlane'] for E in mip_per_plane)
        Nlayer_with_signal = sum(sig > 0 for sig in Nsig_per_plane)
        max_Nhits_per_layer = max(Nsig_per_plane)
        
        if energy_tot<=self.classification_para['Muon']['TotalEnergyDepositMax'] and small_Edeposit_per_stage and Nlayer_with_signal>=self.classification_para['Muon']['NumberOfDetectionPoints'] and max_Nhits_per_layer<=self.classification_para['Muon']['MaximumNumberOfHitsPerPlane']:
            # this might be a muon
            # check chi2
            # for simple events (1 hit per layer), just ust least square:
            chi2 = 0
            if max_Nhits_per_layer==1:
                reg_y, reg_z, m, theta, chi2 = self.fit_event(data,least_squares)
            # for more comlicated events:
            if max_Nhits_per_layer>1 or chi2>self.classification_para['Muon']['MaxChi2']:
                #reg_y, reg_z, m, theta, chi2 = self.fit_event(data,iterative_least_squares)
                reg_y, reg_z, m, theta, chi2 = self.fit_event(data,least_squares,True)
            #reg_y, reg_z, m, theta, chi2 = self.fit_event(data,iterative_least_squares)
            if chi2 <= self.classification_para['Muon']['MaxChi2']:
                fit_results = {'reg_y':reg_y, 'reg_z':reg_z, 'm':m, 'theta':theta, 'chi2':chi2}
                self.cmd['MuonFitPara'].append(fit_results)
                self.cmd['AllEventsMuonFitPara'].append(fit_results)
                """self.fit_results['reg_y'] = reg_y
                self.fit_results['reg_z'] = reg_z
                self.fit_results['m'] = m
                self.fit_results['theta'] = theta
                self.fit_results['chi2']  = chi2"""
                #self.fit_results.append(fit_results)
                self.last_event_type = "Muon"
                return True
        return False
        
    def isElectron(self, Nsig_per_plane, mip_per_plane):
        # Electrons - we want:
        # 1) Large energy deposit > 30 MIPs typically
        # 2) not too many hits per plane (otherwise it's a large energy deposit event (HighElectronEnergy)
        
        energy_tot=sum(mip_per_plane)  # total energy deposit
        
        if (energy_tot>=self.classification_para['Electron']['TotalEnergyDepositMin'] and 
                    max(Nsig_per_plane)<=self.classification_para['Electron']['NumberOfHitsPerPlaneMax']):
            self.last_event_type = "Electron"
            return True
        else:
            return False
    
    def isDisintegration(self, Nsig_per_plane, mip_per_plane):
        # For a disintegration occuring inside the detector, we want:
        # 1) small energy deposit in the first layers
        # 2) large energy in the next layers
        # 3) many hits in these next layers
        
        layers_before = []
        layers_after = []
        for (nsig,mip) in zip(Nsig_per_plane,mip_per_plane):
            if nsig>0:
                if (nsig<=self.classification_para['Disintegration']['Before']['NumberOfHitsPerPlaneMax'] and 
                            mip<=self.classification_para['Disintegration']['Before']['EnergyDepositPerPlaneMax']):
                    # this layer is before the disintegration
                    layers_before.append((nsig,mip))
                elif (nsig>=self.classification_para['Disintegration']['After']['NumberOfHitsPerPlaneMin'] and 
                            mip>=self.classification_para['Disintegration']['After']['EnergyDepositPerPlaneMin']):
                    # this layer is after the disintegration
                    layers_after.append((nsig,mip))
        if (len(layers_before)>=self.classification_para['Disintegration']['Before']['NumberOfLayersMin'] and 
                    len(layers_after)>=self.classification_para['Disintegration']['After']['NumberOfLayersMin']):
            self.last_event_type = "Disintegration"
            return True
        else:
            return False
            
    def isHighE(self, Nsig_per_plane, mip_per_plane):
        # For a large energy deposit event, we want:
        # 1) Large total energy deposit
        # 2) Large energy deposit in each layer
        # 3) Large number of hits
        
        energy_tot=sum(mip_per_plane)  # total energy deposit
        if energy_tot>=self.classification_para['HighEnergyElectron']['TotalEnergyDepositMin']:
            for (nsig,mip) in zip(Nsig_per_plane,mip_per_plane):
                if not (nsig>=self.classification_para['HighEnergyElectron']['NumberOfHitsPerPlaneMin'] and 
                            mip>=self.classification_para['HighEnergyElectron']['EnergyDepositPerPlaneMin']):
                    return False
        else:
            return False
            
        self.last_event_type = "HighEnergyElectron"
        return True
    
    def classify_event(self,data,event):
        ts = time.time()
        counter=[]
        Nbr_Signal_per_Stage,Nbr_Mip_per_Stage=self.signal_per_stage(data)
        data=data.ravel()
        self.data=data
        if(np.all(data==0)==False):
            
            # all events
            self.cmd['AllEvents'].append(data)
            self.event[0].append(event[0])
            self.energie[0].append(self.energie_deposite(data))
            
            if self.isElectron(Nbr_Signal_per_Stage,Nbr_Mip_per_Stage):
                self.cmd['Electron'].append(data)
                self.event[2].append(event[0])
                self.energie[2].append(self.energie_deposite(data))
                self.cmd['AllEventsType'].append("Electron")
                fit_results = {'reg_y':0, 'reg_z':0, 'm':0, 'theta':0, 'chi2':0}
                self.cmd['AllEventsMuonFitPara'].append(fit_results)
            
            elif self.isDisintegration(Nbr_Signal_per_Stage,Nbr_Mip_per_Stage):
                self.cmd['Disintegration'].append(data)
                self.event[3].append(event[0])
                self.energie[3].append(self.energie_deposite(data))
                self.cmd['AllEventsType'].append("Disintegration")
                fit_results = {'reg_y':0, 'reg_z':0, 'm':0, 'theta':0, 'chi2':0}
                self.cmd['AllEventsMuonFitPara'].append(fit_results)
                
            elif self.isHighE(Nbr_Signal_per_Stage,Nbr_Mip_per_Stage):
                self.cmd['HighEnergyElectron'].append(data)
                self.event[4].append(event[0])
                self.energie[4].append(self.energie_deposite(data))
                self.cmd['AllEventsType'].append("HighEnergyElectron")
                fit_results = {'reg_y':0, 'reg_z':0, 'm':0, 'theta':0, 'chi2':0}
                self.cmd['AllEventsMuonFitPara'].append(fit_results)
                
            elif self.isMuon(data,Nbr_Signal_per_Stage,Nbr_Mip_per_Stage):
                self.cmd['Muon'].append(data)
                self.event[1].append(event[0])
                self.energie[1].append(self.energie_deposite(data))
                self.cmd['AllEventsType'].append("Muon")
                
            else: # all other event that are not classified
                self.last_event_type = "NotClassified"
                self.cmd['AllEventsType'].append("NotClassified")
                fit_results = {'reg_y':0, 'reg_z':0, 'm':0, 'theta':0, 'chi2':0}
                self.cmd['AllEventsMuonFitPara'].append(fit_results)
                
        return self.cmd
        
                                    
    def parameters(self):
        with open(self.setup_path,'r') as f:
            cfg=yaml.load(f)
        
        self.classification_para = dict(cfg['ClassificationParameters'])
        
        log.info("Classification parameters loaded from file: {}".format(self.setup_path))
        #self.elecron_energie_per_plane=cfg['Electron']['EnergieLimitePerPlane']
        #self.elecron_nb_etage=cfg['Electron']['PlaneNumber']
        
    def energie_deposite(self,data):   
        # renvoie l'energie totale de la trace
        signal_per_stage,mip_per_stage=self.signal_per_stage(data)
        energie_tot=sum(mip_per_stage)
        return int(round(energie_tot))
    
    def energie_deposite_seperete(self): 
        #array event energie [All,Muon,....]
        return self.energie
        
    def event_id(self):      
        #array event id [All,Muon,....]
        return self.event
    
    def print_signal(self):
        #Affiche les donnees sur le terminal () representation detecteur
        self.signal_per_stage()          
        for i,value in enumerate(self.data.ravel()):
            print(round(value,3),' ', end='')
            if((i+1)%self.Sensor_per_Stage==0):
                print("\n")
        print(len(data),"\n")
    
    
    def simulation_x(self,data):
        # simule un tableau pour la troisième dimension du detecteur
        coef=1;x=[];
        if(np.all(data==0)==True):          # si pas de signal 
            x=[int(i) for i in self.acq_proc.y_coords]
        else:
            if(self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos!=self.securite_random):
                coef=rand.randrange(-10,10)
                self.securite_random=self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos
                if(coef==0):
                    coef=1
            for i in range(len(self.acq_proc.y_coords)):
                if(-5<(self.acq_proc.y_coords[i]-5)/coef<5):
                    x.append((self.acq_proc.y_coords[i]-5)/coef)
                else:
                    x.append(5)
        return x
        
    def signal_xyz(self,data):
        # calculate the position along the bar axes
        # renvoie pour chaque point, sa quantité de signal sa position xyz une matrice contenant les deux points du fit pour le muon
        y=[];z=[];x=[];signal=[];coef=1
        verts=np.empty((2, 1, 3), dtype=float)
        for j, i in enumerate(data):
            if(i!=0):
                for i_z in range(len(self.acq_proc.y_coords)):
                    if(i_z==j):
                        z.append(self.acq_proc.y_coords[i_z])
                for i_y in range(len(self.acq_proc.x_coords)):
                    if(i_y==j):
                        y.append(self.acq_proc.x_coords[i_y])
                signal.append(i)
        if not signal:          # si pas de signal 
            for i in range(len(y)):
                x.append(0)
        else:
            if(self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos!=self.securite_random):
                coef=rand.randrange(-10,10)
                self.securite_random=self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos
                if(coef==0):
                    coef=1
            for i in range(len(y)):
                if(-5<(y[i]-5)/coef<5):
                    x.append((y[i]-5)/coef)
                else:
                    x.append(5)
        return y,z,x
        
    def fit_event3D(self,data,pos):
        pos_signal = np.empty((self.acq_proc.num_sensors_enabled, 3),dtype=int)
        verts=np.empty((2, 1, 3), dtype=float)
        counter=0
        for j, i in enumerate(data):
            if(i!=0):
                pos_signal[counter]=pos[j]
                counter+=1
        pos_signal[1]=pos_signal[counter-1]
        pos_signal[0]=10*(pos_signal[0]-pos_signal[1])+pos_signal[0]
        pos_signal[1]=-10*(pos_signal[0]-pos_signal[1])+pos_signal[1]
        return pos_signal[0:2]             
        
    def fit_event(self,data,fittype=iterative_least_squares,PatRec=False):
    
        # new regression with least squares method
        theta = 0   # theta is the angle from the vertical (y)
        y,z,x = self.signal_xyz(data)
        #m, z0, chi2 = least_squares(y,z)
        #m, z0, chi2 = iterative_least_squares(y,z)
        if PatRec:
            yout,zout = reject_hits_pattern_recognition2(y,z,self.x_para,self.y_para,2.5)
            if len(yout)>2 and len(zout)>2:
                m, z0, chi2 = fittype(yout,zout)
            else:
                return [0], [0], 0, 0, 1000
        else:
            m, z0, chi2 = fittype(y,z)
        
        # pattern recognition:
        #reject_hits_pattern_recognition(y,z,self.x_para,self.y_para,1)
        #reject_hits_pattern_recognition2(y,z,self.x_para,self.y_para,2)
        
        xmin = self.x_para["min"] - 0.5*self.x_para["pitch"]
        xmax = self.x_para["max"] + 0.5*self.x_para["pitch"]
        ymin = self.y_para["min"] - 0.5*self.y_para["pitch"]
        ymax = self.y_para["max"] + 0.5*self.y_para["pitch"]
        
        reg_y, reg_z = [], []
        if(m is None) : ## straight vertical tracks
            theta = 0
            reg_y = [ z0,z0 ]
            reg_z = [ ymin,ymax ]
        elif(m == 0):
            theta = 90
            reg_y = [ xmin,xmax ]
            reg_z = [ z0,z0 ]
        else :
            theta  = (180/math.pi)*math.atan(-1./m)
            y_intersect_xmin = m*xmin + z0
            y_intersect_xmax = m*xmax + z0
            x_intersect_ymin = (ymin-z0)/m
            x_intersect_ymax = (ymax-z0)/m
            if xmin <= x_intersect_ymin <= xmax:
                reg_y.append(x_intersect_ymin)
                reg_z.append(ymin)
            if xmin <= x_intersect_ymax <= xmax:
                reg_y.append(x_intersect_ymax)
                reg_z.append(ymax)
            if ymin < y_intersect_xmin < ymax:
                reg_y.append(xmin)
                reg_z.append(y_intersect_xmin)
            if ymin < y_intersect_xmax < ymax:
                reg_y.append(xmax)
                reg_z.append(y_intersect_xmax)
                
        print("m=",m,"   theta=",theta,"   chi2=",chi2)
        return reg_y, reg_z, m, theta, chi2
        
############################### non utilisé ###########################    
    def angle(self,data):                                                                                                                                                                                   
        angle=data
        nbr=0
        nbr_ev=[]
        val_theta=[]
        for i,theta in enumerate(angle):
            if(theta!=0):
                val_theta.append(theta)
                for i2,theta2 in enumerate(angle):
                    if(theta2==theta or theta2==-theta):
                        nbr+=1
                        angle[i2]=0
                nbr_ev.append(nbr)
                nbr=0
        print(nbr_ev,np.round(val_theta),x,y)
        return np.asarray(nbr_ev),np.asarray(val_theta) 
        
    def class_muon(self):
        for j, i in enumerate(Nbr_Signal_per_Stage):
            if(i==1 and Nbr_Mip_per_Stage[j]<35/self.acq_proc.PetoMip):
                counter.append(1)
                if(sum(counter)==3 and j==2):
                    for j,i in enumerate(Nbr_Signal_per_Stage[3:]):
                        if(i==1 and Nbr_Mip_per_Stage[j]<35/self.acq_proc.PetoMip):   ####  Muon
                            counter.append(1)
                            if(sum(counter)>=len(Nbr_Signal_per_Stage)-2 and j==len(Nbr_Signal_per_Stage)-4):
                                self.cmd['Muon'].append(data)
                                self.event[1].append(event[0])
                                self.energie[1].append(self.energie_deposite(data))
            if(i==0):counter.append(0)
    
    def class_electron(self):
        for j, i in enumerate(Nbr_Signal_per_Stage):
            if(i==1 and Nbr_Mip_per_Stage[j]<35/self.acq_proc.PetoMip):
                counter.append(1)
                if(sum(counter)==3 and j==2):
                    for j,i in enumerate(Nbr_Signal_per_Stage[3:]):
                        if(i>1 and Nbr_Mip_per_Stage[j]>20/self.acq_proc.PetoMip):    ####  Electron
                            self.cmd['Electron'].append(data)
                            self.event[2].append(event[0])
                            self.energie[2].append(self.energie_deposite(data))
            if(i==0):counter.append(0)
    
    def class_mon_decay(self):
        for j, i in enumerate(Nbr_Signal_per_Stage):
                if(i==1 and Nbr_Mip_per_Stage[j]<35/self.acq_proc.PetoMip):
                    counter.append(1)
                    if(sum(counter)==3 and j==2):
                        x,y,signal=self.signal_xy(self.data)
                        a=(y[0]-y[2])/(x[0]-x[2])
                        b=y[0]-a*x[0]
                        for i in x:
                            reg_y.append(a*i + b)
    
    def class_electron_E(self):
        print()
    
