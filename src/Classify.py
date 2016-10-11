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
        self.theta=[]
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
                                    self.theta.append(self.fit_event(data,plot=False))
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
        return self.cmd,np.asarray(self.theta)
        
                                    
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
    
        # new regression with least squares method
        theta = 0
        y,z,x = self.signal_xyz(data)
        m, z0 = least_squares(y,z)
        #m, z0 = iterative_least_squares(y,z)
        reg_y, reg_z = y, []
        
        if(m is None) : ## straight vertical tracks
            theta = 90
            reg_z = np.arange(1,len(y)+1)
        else :
            reg_y = []
            theta  = (math.atan(m)*180.)/math.pi
            for zi in z :
                yr = (zi - z0)/m
                if 0 < yr < 33 : 
                    reg_y.append( yr )
                    reg_z.append( zi )
            #if(plot==True):print (m, z0, theta)
        
        if(plot==True):
            return reg_y, reg_z
        return theta 
            
            
        
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
                                self.theta.append(self.fit_event(data,plot=False))
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
    

################################################

## Lest_squares is the one that works.
## Iterative least_squares repeates the least_squares weighting the points by the inverse of the residual
## meaning that points far away become less and less important. Fit stops when the angular coessificent
## changes less than 10% from the previous iteration. (To be tested!!!) 

def get_weights(m,y0,x,y,w) :
    
    nw = []
    if len(w) == 0 : w = [1.]*len(x)
    for x,y in zip(x,y) :
        res = y - ( m*x + y0 )
        nw.append(w * 1./res)
    return nw

def iterative_least_squares(x,y) :
    
    w = [1.]*len(x)
    prevm = -999999
    m, y0 = 0, 0
    print("Iterative fitting")
    while True :
        
        if m is None:
            break;
        m,y0 = least_squares_w(x,y,w)
        print (m, y0)
        if abs(m - prevm)/m < 0.1 : break
        prevm = m
        
        w = get_weights(m,y0,x,y,w)
    
    return m,y0

def least_squares( x, y ) :

    if len(x) != len(y) :  
        print("ATTENTION: x and y have different lenghts, no fit performed")
        return
        
    N = len(y)
    mean_x = sum( x ) / float(N)
    denom = sum( [ (xi - mean_x)**2 for xi in x ] )
    if denom < 1.e-6 : return None, x[0]
    
    mean_y = sum( y ) / float(N)
    
    xy = []
    for xi,yi in zip(x,y) :
        xy.append((xi - mean_x)*(yi - mean_y))
    
    sum_xy = sum( xy )
    m = sum_xy / denom 
    y0 = mean_y - m*mean_x
    
    return m,y0

def least_squares_w( x, y, w ) :

    if len(x) != len(y) :  
        print("ATTENTION: x and y have different lenghts, no fit performed")
        return
        
    sumw = sum(w)
    x,y,x2,xy = [],[],[],[]
    for xi,yi,wi in zip(x,y,w) :
        x.append(wi*xi)
        y.append(wi*yi)
    
    mean_x =  sum(x) / float(sumw)
    
    for xi,yi,wi in zip(x,y,w) :
        xy.append(wi*(xi - mean_x)*(yi - mean_y))
        x2,append(wi*(xi - mean_x)**2)
    
    denom = sum(x2)
    if denom < 1.e-6 : return None, None
    
    mean_y = sum( y ) / float(sumw)
    
    sum_xy = sum( xy )
    m = sum_xy / denom 
    y0 = mean_y - m*mean_x
    
    return m,y0
