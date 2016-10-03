#!/usr/bin/python3
import multiprocessing
import sys
import time
import platform
import itertools
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import math as m
import random as rand


import logging as log
import logging.handlers
import argparse

from LiveWindow import *
from CommandWindow import *
from SavedWindow import *

from acqprocessing import AcqProcessing
from ringbuffer2d import RingBuffer2D


class Classify(object):   
# object qui renvoie un dictionnaire trié
# Il possède une fonction de trie 
#            une fonction donnant l'energie deposée
#            une fonction donnant le nombre de sensors ayant recu du signal
#......

    def __init__(self,cmd,sensorpath,setuppath):    #cmd = dico Live (Class_EventLive) or dico Saved  (Class_EventSaved)  #data = Tableau 2D
        self.acq_proc=AcqProcessing()
        self.cmd=cmd # dico 
        self.teta=[]
        self.sensors_path=sensorpath
        self.setup_path=setuppath
        self.key="live"
        self.event=[[],[],[],[],[]]     #[eventAll,eventMuon,eventElectron,eventMuonDecay,eventHighEnergieElectron]
        self.energie=[[],[],[],[],[]]   
        self.securite_random=0
        self.configure()
        self.i=0

    def configure(self):
        data = np.genfromtxt(self.sensors_path, dtype=np.float)
        self.acq_proc.load_general_setup_file(self.setup_path)
        self.acq_proc.set_sensor_pos(data[:,5], data[:,4], data[:,0], data[:,1])
        
        
        
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
        
    def classify_event(self,data,event):
        ts = time.time()
        counter=[]
        Nbr_Signal_per_Stage,Nbr_Mip_per_Stage=self.signal_per_stage(data)
        data=data.ravel()
        self.data=data
        if(np.all(data==0)==False):
            self.cmd['AllEvents'].append(data)
            self.event[0].append(event[0])
            self.energie[0].append(self.energie_deposite(data))
            for j, i in enumerate(Nbr_Signal_per_Stage):
                if(i==1 and Nbr_Mip_per_Stage[j]<35/self.acq_proc.PetoMip):
                    counter.append(1)
                    if(sum(counter)==3 and j==2):
                        for j,i in enumerate(Nbr_Signal_per_Stage[3:]):
                            if(i==1 and self.energie_deposite(data)<140/self.acq_proc.PetoMip):   ####  Muon
                                counter.append(1)
                                if(sum(counter)>=len(Nbr_Signal_per_Stage)-2 and j==len(Nbr_Signal_per_Stage)-4):
                                    self.cmd['Muon'].append(data)
                                    self.event[1].append(event[0])
                                    self.energie[1].append(self.energie_deposite(data))
                                    self.teta.append(self.fit_event(data,plot=False))
                            if(i==0):counter.append(0)
                            if(i>1 and Nbr_Mip_per_Stage[j]>20/self.acq_proc.PetoMip):    ####  Electron
                                self.cmd['Electron'].append(data)
                                self.event[2].append(event[0])
                                self.energie[2].append(self.energie_deposite(data))
                            if(i>2 and self.energie_deposite(data)>140/self.acq_proc.PetoMip ):
                                self.cmd['MuonDecay'].append(data)
                                self.event[3].append(event[0])
                                self.energie[3].append(self.energie_deposite(data))
                else:counter.append(0)
            if(self.energie_deposite(data)>1100/self.acq_proc.PetoMip):
                self.cmd['HighEnergieElectron'].append(data)
                self.event[4].append(event[0])
                self.energie[4].append(self.energie_deposite(data))
        te = time.time()
        #print("{}",format(te-ts))
        return self.cmd,np.asarray(self.teta)
        
                                    
    def parameters(self):
        with open(self.setup_path,'r') as f:
            cfg=yalm.load(f)
        self.muon_energie = cfg['Muon']['EnergieDeposite']
        self.muon_detect_point = cfg['Muon']['DetectionPointNumber']
        self.muon_point_per_plane= cfg['Muon']['PointPerPlane']
        self.elecron_energie_per_plane=cfg['Electron']['EnergieLimitePerPlane']
        self.elecron_nb_etage=cfg['Electron']['PlaneNumber']
        
        
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
        
    def fit_event(self,data,plot=True):     
        # regression on the first and the last point, muon fit
        y=[];z=[];reg_z=[]
        a=0;b=0;teta=0
        y,z,x=self.signal_xyz(data)
        if(y[0]-y[len(y)-1]!=0):
            a=(z[0]-z[len(z)-1])/(y[0]-y[len(y)-1])
            b=z[0]-a*y[0]
            teta=(m.atan(1/a)*180)/m.pi
            for i in y:
                reg_z.append(a*i + b)
        if(y[0]-y[len(y)-1]==0):
            z=[0]*len(z)
            reg_z=np.arange(0,len(y))
        if(plot==True):
            return y, reg_z
        if(plot==False): 
            return teta 
            
            
        
############################### non utilisé ###########################    
    def angle(self,data):  
        angle=data
        nbr=0
        nbr_ev=[]
        val_teta=[]
        for i,teta in enumerate(angle):
            if(teta!=0):
                val_teta.append(teta)
                for i2,teta2 in enumerate(angle):
                    if(teta2==teta or teta2==-teta):
                        nbr+=1
                        angle[i2]=0
                nbr_ev.append(nbr)
                nbr=0
        print(nbr_ev,np.round(val_teta),x,y)
        return np.asarray(nbr_ev),np.asarray(val_teta) 
        
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
                                self.teta.append(self.fit_event(data,plot=False))
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
    ##


