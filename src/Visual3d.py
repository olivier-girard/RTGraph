import multiprocessing
import sys
import time
import platform
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph.opengl as gl
import math as m
import logging as log
import logging.handlers
import argparse

from CommandWindow import *
from acqprocessing import AcqProcessing

class View3D:
    
    def __init__(self,graph,acq_proc):
        self.acq_proc=acq_proc
        self.w = gl.GLViewWidget()
        self.w.setWindowTitle('3D')
        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(0, 0, 0)
        self.w.addItem(gx)
        self.graph=graph
        self.graph.opts['distance'] = 40
        self.graph.opts['azimuth']=-20
        self.graph.opts['elevation']=15
        self.graph.pan(0,0,0)
        self.i=0
        self.nbpoint=0
        self.box_barette=self.draw_box(0,0,0)
        self.box_signal=self.draw_box(0,0,0)
        self.barette=[gl.GLMeshItem(meshdata=self.box_barette,smooth=True, color=(0.1,0.5,0.5,0.05), shader='balloon', glOptions='additive')]*500
        self.rectangle=[gl.GLMeshItem(meshdata=self.box_signal, smooth=True, color=(0.5, 0.2, 0.1, 0.3), shader='shaded', glOptions='additive')]*100#gl.GLMeshItem(meshdata=self.sph, smooth=True, color=(0.5, 0.2, 0.1, 0.3), shader='balloon', glOptions='additive')
        
        self.timer_camera(0.2)

    def timer_camera(self,s):  # timer de mouvement 
        self.timer_cam=QtCore.QTimer()
        self.timer_cam.timeout.connect(lambda: self.move_camera(s))
    
    def move_camera(self,s):
        # fonction permetant de choisir le mouvement de la camera
        rotation_angle=20  # total rotation angle in deg
        rotation_speed=0.8  #  increase speed to rotate faster
        self.i+=1
        a=self.i%(200/rotation_speed)
        if(0<a<(100/rotation_speed)):
            step=s
        else:step=-s
        self.graph.orbit(step*rotation_angle/50*rotation_speed,step*rotation_angle/50*rotation_speed)   

                        
    def draw_box(self,L,l,h):
        # creer un rectangle de dimansion voulu a la coordonnee 0,0,0  
        # pour le deplacer utiliser translate
        verts=np.empty((8, 1, 3), dtype=float)
        verts[...,0]=np.array([l/2,l/2,-l/2,-l/2,l/2,l/2,-l/2,-l/2]).reshape(8,1)
        verts[...,1]=np.array([L/2,-L/2,-L/2,L/2,L/2,-L/2,-L/2,L/2]).reshape(8,1)
        verts[...,2]=np.array([h,h,h,h,0,0,0,0]).reshape(8,1)
        faces=np.empty((12,3),dtype=np.uint)
        faces=np.array([
        [1,3,0],
        [3,4,0],
        [1,5,0],
        [4,5,0],
        [1,2,3],
        [1,2,5],
        [2,3,7],
        [3,4,7],
        [4,5,7],
        [5,6,7],
        [5,6,2],
        [2,6,7],
        ])
        return gl.MeshData(vertexes=verts, faces=faces)
        
    
    def module(self,taille): #taille [largeur,longueur, hauteur]   geometrie [matrice position]
        # trace le detecteur 
        for j in range (len(self.acq_proc.x_coords)):
            self.box_barette=self.draw_box(taille[0],taille[1],taille[2])
            self.barette[j]=gl.GLMeshItem(meshdata=self.box_barette,smooth=True, color=(0.1,0.5,0.5,0.05), shader='balloon', glOptions='additive')
            self.barette[j].translate(0,-self.acq_proc.Sensor_per_Stage/2+self.acq_proc.x_coords[j],-self.acq_proc.nb_Stage/2 + self.acq_proc.y_coords[j])
            self.w.addItem(self.barette[j])
    

    def affichage(self,intensity,x):
        # affiche le signal sous la forme de rectangle    * rectangle scatter plot
        counter=0
        #etage=8
        #sensor=0
        for i in range(self.nbpoint): 
            self.w.removeItem(self.rectangle[i])
        if(np.max(intensity)!=0):
            intensity=intensity/np.max(intensity)
            for j,i in enumerate(intensity):
                if(i!=0):
                    self.box_signal=self.draw_box(0.8*i,i*2,1/4*i)
                    self.rectangle[counter]=gl.GLMeshItem(meshdata=self.box_signal,smooth=True, color=(i/3,1,0,1), shader='balloon', glOptions='additive')
                    self.rectangle[counter].translate(x[j],-self.acq_proc.Sensor_per_Stage/2 + self.acq_proc.x_coords[j],-self.acq_proc.nb_Stage/2 + self.acq_proc.y_coords[j])        #-self.acq_proc.Sensor_per_Stage/2+self.acq_proc.x_coords[j],-self.acq_proc.nb_Stage+self.acq_proc.y_coords[j])
                    self.w.addItem(self.rectangle[counter])
                    counter+=1
        self.nbpoint=counter

##### non utilisé ##################################3
               
    def box(self,pos=(0,0,0),lenght=0,large=0,delete=0):   ## trop lourd
        k=0;n=0;a=pos[0];b=pos[1];c=pos[2]
        axe=[[0,0,1],[0,1,0],[1,0,0]]
        trans=[[0+a,0+b,0+c],[0+a,0+b,1/4+c],[0+a,0+b,0+c]]
        taille=[[lenght/10,large/10,1],[1/40,large/10,1],[lenght/10,1/40,1]]
        large=[[0,1/4],[0,lenght],[0,-large]]
        if(lenght!=0 or large!=0):
            for j in range(3):
                if(0<j<2):
                    k+=1
                for i in range(2):
                    z = np.empty((11,11),dtype=float)
                    z.fill(large[j][i])
                    self.pp=gl.GLSurfacePlotItem(z=z,shader='shaded', color=(0.7, 0.8, 1, 1))#self.ppsetData(z=z,colors=(0.7, 0.8, 1, 1))
                    self.pp.scale(taille[j][0],taille[j][1],taille[j][2])
                    self.pp.rotate(90*k,axe[j][0],axe[j][1],axe[j][2])
                    self.pp.translate(trans[j][0],trans[j][1],trans[j][2])
                    self.w.addItem(self.pp)
                    self.w.show()
                    n+=1
                    if(delete==1):
                        self.w.removeItem(self.pp)

    def dim(self):
        ## Draw tracker
        k=1
        xt=-5;yt=-12.5;zt=-4   # 0.5
        while(k!=9):
            for i in range(16):
                x = np.linspace(0,10,10)
                y = np.array([i+5]*10)
                z = np.array([k]*10)
                pts = np.vstack([x,y,z]).transpose()
                sp0 = gl.GLLinePlotItem(pos=pts, color=pg.glColor((1,2)), width=0.001,antialias=False)
                sp0.translate(xt,yt,zt)
                self.w.addItem(sp0)
            for i in range (2):
                x=np.array([i*10]*10)
                y=np.linspace(5,20,10)
                pts = np.vstack([x,y,z]).transpose()
                sp1 = gl.GLLinePlotItem(pos=pts, color=pg.glColor((1,2)), width=0.001,antialias=False)
                sp1.translate(xt,yt,zt)
                self.w.addItem(sp1)
            for i in range(16):
                x = np.linspace(0,10,10)
                y = np.array([i+5]*10)
                z = np.array([1/4+k]*10)
                pts = np.vstack([x,y,z]).transpose()
                sp2 = gl.GLLinePlotItem(pos=pts, color=pg.glColor((1,2)), width=0.001,antialias=False)
                sp2.translate(xt,yt,zt)
                self.w.addItem(sp2)
            for i in range (2):
                x=np.array([i*10]*10)
                y=np.linspace(5,20,10)
                pts = np.vstack([x,y,z]).transpose()
                sp3 = gl.GLLinePlotItem(pos=pts, color=pg.glColor((1,2)), width=0.001,antialias=False)
                sp3.translate(xt,yt,zt)
                self.w.addItem(sp3)
            for n in range(2):
                for i in range(16):
                    z=np.linspace(k,k+1/4,10)
                    x=np.array([n*10]*10)
                    y=np.array([i+5]*10)
                    pts = np.vstack([x,y,z]).transpose()
                    sp4 = gl.GLLinePlotItem(pos=pts, color=pg.glColor((1,2)), width=0.001,antialias=False)
                    sp4.translate(xt,yt,zt)
                    self.w.addItem(sp4)
            k+=1
