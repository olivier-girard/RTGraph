#!/usr/bin/python3
import multiprocessing
import sys
import time
import platform
import itertools
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph.opengl as gl
import os
import math
import csv
import select

import logging as log
import logging.handlers
import argparse

from LiveWindow import *
from CommandWindow import *
from SavedWindow import *
from PosterWindow import *
#from AutoWindow import *

from acqprocessing import AcqProcessing
from Classify import Classify
from Visual3d import View3D

from triggers import triggers
from configurePlots import pt_size, pt_colour

# architecture: le programme est divisé en trois parties, une pour chaque pannel:live, command et saved
# les configurations des trois fenètres s'effectue grâce a deux fichiers, le SetupFile qui contient 
# les gains, les entrées et les paramètrees trie et le GEOnmetrieFile qui dimentionne le detecteur 
# Live a besoin de la bibliotheque d'acquisition acqprocessing pour prendre les donnees les traiter et les ploter
# Saved traite les donnees et les traces directements
# les donnees arrivent dans le programme, sont traitees (retrait du bruit et conversion en p.e ou MIP)
# Elles sont ensuite classée avec l'object Classify qui renvoie un dictionnaire 
# le dictionnaire live s'enregistre dans un fichier tout les ... voir taille du buffer self.acq_proc.num_integrations

class AutoWindow(QtGui.QMainWindow):
    
    def __init__(self):
    
        QtGui.QMainWindow.__init__(self)                          #     objet fenetre live
        self.ui = Ui_MainWindow()                                 #
        #self.ui.setupUi(self)
        
        self.img = pg.ImageItem()                                           # image channel
        self.Hist=pg.PlotCurveItem()                                        # histogramme 
        self.FreqHist=pg.PlotCurveItem(stepMode=False)                      # histogramme
        self.scatt = pg.ScatterPlotItem(pxMode=False,pen=pg.mkPen(None))    # scatter plot
        self.droite = pg.PlotDataItem(x=[],y=[],pen=pg.mkPen(color='g',width=3))                            # track fit
        self.module=[pg.GraphItem()]*400
        
        self.curdisplay = self.ui.autoplot.addPlot(title ="")
        self.curdisplay.addItem(self.Hist)
        self.curitems = [self.Hist]
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.change_display)
        
        self.curstep = 0
        self.steps = [ 
        				[self.scatt,self.droite],
        				[self.Hist],
        				[self.FreqHist]
        				]
        
        while True :
        	print ("Looping 5 seconds step")
            time.sleep(5)
            self.change_display()
        
    def set_data(self,hist,freq,scatt,line) :
    
        #self.Hist.setData(hist)                            
        #self.FreqHist.setData(freq)				                  
        #self.scatt.setData(scatt)					  
        #self.droite.setData(line)
		self.Hist     = hist
		self.FreqHist = freq
		self.scatt    = scatt
		self.droite   = line

    def change_display(self) :
    
        prevstep = self.curstep
        if self.curstep < (len(self.steps)-1) :
        	self.curstep += 1
        else :
        	self.curstep = 0
        	 
        for it in self.steps[prevstep] :
        	self.curdisplay.removeItem(it)
        for it in self.steps[self.curstep] :
        	self.curdisplay.addItem(it)

class LiveWindow(QtGui.QMainWindow):
    
    integrate_on = False
    
    def __init__(self, acq_proc):
        QtGui.QMainWindow.__init__(self)      #     objet fenetre live
        self.ui = Ui_MainWindow()    
        self.ui.setupUi(self)  
        
        self.Auto=AutoWindow() 
        
        # Know about an instance of acquisition/processing code
        # to forward GUI events
        self.acq_proc = acq_proc    # object acquisition
        self.view3d=View3D(self.ui.plt3d,acq_proc)    #     object 3d
        
        self.timer_plot_update = None
        self.timer_freq_update = None
        self.live_mode = True   # live mode set to True. Set to False when we push the pause button
        self.start_time = time.time()
        self.tsampled = []                              ## sampling time
        self.vsampled = { "freq" : [], "nevt" : [] }    ## sampled variables
        self.sample_dt = 5                              ## sampling interval
        
        self.sp = None
        self.nb_events_per_class=[0]*5                                   #  nbr de categorie d'evenement differents  ex: All,Muon,Electron.....
        self.event_name=['AllEvents','Muon','Electron','Disintegration','HighEnergyElectron']      # nom des categories
        self.nbr_saving=[0]*5                                            # nbr de sauvegarde pour chaque categorie
        self.event_seperete=[[0]]*5
        self.energie_tot_seperete=[[0]]*5
        self.play_cam=1                                                  # booleen camera 3d
        
        #trigger
        self.trigger_dec = True
        self.trigger_type = "nlayers"
        
        ## For integration
        self.path_calib = "./mip_calibration.csv"
        self.calibrate_MIP = True
        self.mip_calibration = []
        self.int_events = 0
        self.calib_events = 0
        self.int_intensities = []
        self.int_colors = []
        self.theta = []
        
        # configures plots
        self.configure_plot()
        self.slope_conversion_factor = 1    # conversion of slope in 2D plot and in reality
        #if not self.calibrate_MIP : self.load_calibration()    # to load calibration file and "append" it
        
        self.Auto.set_data(self.Hist,self.FreqHist,self.scatt,self.droite)
        self.Auto.show()


        # CONFIGURATION
    def configure_plot(self):
        # object plot 2D
        self.img = pg.ImageItem()                                           # image channel
        self.Hist=pg.PlotCurveItem()                                        # histogramme 
        self.FreqHist=pg.PlotCurveItem(stepMode=False)                      # histogramme
        self.scatt = pg.ScatterPlotItem(pxMode=False,pen=pg.mkPen(None))    # scatter plot
        self.droite = pg.PlotDataItem(x=[],y=[],pen=pg.mkPen(color='g',width=3))                            # track fit
        self.module=[pg.GraphItem()]*400
        self.pb_plates=[None]*5       # Pb plates
        # matrice 3D
        self.pos3D = np.empty((self.acq_proc.num_sensors_enabled, 3))
        self.size3D = np.empty(self.acq_proc.num_sensors_enabled)
        self.color3D = np.empty((self.acq_proc.num_sensors_enabled, 4))
        # Object plot 3D
        self.scat3d = gl.GLScatterPlotItem(pos=self.pos3D, size=self.size3D, color=self.color3D, pxMode=False)
        self.fit3d = gl.GLLinePlotItem(pos=self.pos3D,color=pg.glColor((0,1.3)), width=1, antialias=True)
        self.view3d.w.addItem(self.scat3d)
        self.view3d.w.addItem(self.fit3d)
        # Graphiques
        self.channel = self.ui.pltchannel.addPlot(title ="Channels")                       
        self.channel.addItem(self.img) 
        self.tracker = self.ui.plttracker.addPlot(title ="Tracker")
        self.tracker.addItem(self.droite)
        self.tracker.addItem(self.scatt)
        self.histogram = self.ui.plthistogram.addPlot(title = 'Angle Incidencie')
        self.histogram.addItem(self.Hist)
        self.frequency = self.ui.pltfrequency.addPlot(title="Event Frequency")
        self.frequency.addItem(self.FreqHist)
        
    def setRange2Dplot(self):
        # set 2D plot range
        spacing_x = np.unique(self.acq_proc.x_coords)[1] - np.unique(self.acq_proc.x_coords)[0]
        minx = np.unique(self.acq_proc.x_coords)[0]
        maxx = np.unique(self.acq_proc.x_coords)[-1]
        spacing_y = np.unique(self.acq_proc.y_coords)[1] - np.unique(self.acq_proc.y_coords)[0]
        miny = np.unique(self.acq_proc.y_coords)[0]
        maxy = np.unique(self.acq_proc.y_coords)[-1]
        self.scatt.getViewBox().setXRange(minx-0.5*spacing_x, maxx+0.5*spacing_x, padding=None)
        self.scatt.getViewBox().setYRange(miny-0.5*spacing_y, maxy+0.5*spacing_y, padding=None)
        self.scatt.getViewBox().disableAutoRange()
        
    def configure_timers(self):
        self.timer_plot_update = QtCore.QTimer(self)
        self.timer_acquisition = QtCore.QTimer(self)
        self.timer_acquisition.timeout.connect(self.fill_dico)    # acquisition a chaque click d'horloge
        self.timer_plot_update.timeout.connect(self.update_plot)  # update plot a chaque click
        self.view3d.timer_cam.start(10)                           # rotation camera
        
        #TIMER choose the event wanted display on the plot
    def timer(self,cmd="right"):         ## change data array position
        if(cmd=="left" and self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos>0 ):
            self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos-=1
        if(cmd=="right" and self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos<self.acq_proc.Class_EventLive[self.acq_proc.option].len()-1):
            self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos+=1
        
        #UPDATE PLOT    plot 1*3d, 1*2d, 2*histogrammes,  
    def update_plot(self):
        
        if self.live_mode:
            if not self.trigger_dec:
                return
            if self.acq_proc.evNumber.get_partial()[0] == self.acq_proc.last_event_plotted:
                # the event has already been plotted
                return
                
        current_pos=self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos
        if( self.acq_proc.plot_signals_scatter()==False ):                                                            # mistake between sensorenable and datapipe lenght
            self.timer_plot_update.stop()
            return
        
        if self.acq_proc.option!="AllEvents":
            event_type = self.acq_proc.option
            fit_para_key = "MuonFitPara"
        else:
            event_type = self.acq_proc.Class_EventLive["AllEventsType"][self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos][0]
            fit_para_key = "AllEventsMuonFitPara"
        
        print("Event:",self.acq_proc.evNumber.get_partial()[0],"  Type:",event_type)
        self.event_type = event_type

        intensity, self.data = self.acq_proc.plot_signals_scatter()
        
        mini_size = 0.1
        if self.integrate_on:
            intensity = self.integrate(intensity)
            mini_size = 0.01
        
        # channel histogram
        self.img.setImage(self.data.reshape(self.acq_proc.num_sensors_enabled,1))                                 # affiche histogramme channel
        
        # 2D scatter plot
        maxintensity = np.max(intensity)
        if(maxintensity!=0):
            # point size and colour are defined in file configurePlots.py
            self.scatt.setData(x=self.acq_proc.x_coords,y=self.acq_proc.y_coords,
                size=pt_size["linear"](intensity,maxi=1,mini=mini_size,saturate_at=0.5),
                brush=pt_colour["linear"](intensity,maxi=0,mini=90)) # plot scatter
        if (not self.integrate_on) and event_type=="Muon":
            if self.live_mode:
                posi = current_pos+1
            else:
                posi = current_pos
            reg_y = self.acq_proc.Class_EventLive[fit_para_key][posi][0]['reg_y']
            reg_z = self.acq_proc.Class_EventLive[fit_para_key][posi][0]['reg_z']
            self.droite.setData(reg_y,reg_z)
        else:
            self.droite.setData([0],[0])     # resets linear fit to nothing
        
        # checks if autorange is on: if yes, disable it
        if self.scatt.getViewBox().getState()['autoRange'] == [True, True]:
            self.setRange2Dplot()
        
        ###### 3D #######
        if not self.integrate_on:
            y,z,x_coord=self.dico_live.signal_xyz(intensity)                    # give coordonee(x_coord,y,z), signal in MIP or p.e and two points(verts) to plot fiting muon trace
            x_coords=self.dico_live.simulation_x(intensity)
            for i in range(len(self.acq_proc.y_coords)):
                self.color3D[i]=(1,1,1,1)                                       # COULEUR SCATTER3D
        # array contenant les donnees 3d 
            self.pos3D=np.vstack([x_coords,-self.acq_proc.Sensor_per_Stage/2+self.acq_proc.x_coords,-self.acq_proc.nb_Stage/2 + self.acq_proc.y_coords]).transpose()
            if(maxintensity!=0):
        #self.scat3d.setData(pos=self.pos3D,size=np.asarray(intensity)/maxintensity,color=self.color3D) # charge les donnees
                self.scat3d.setData(pos=self.pos3D,size=pt_size["linear"](intensity,maxi=1,mini=0.1),color=self.color3D) # charge les donnees
            self.view3d.affichage(intensity,x_coords)  # affiche le graph 3d    # x_coord= coordonnées simulées des rectangles 
            if(self.option_num==1):
            # the third dimension is calculated with random
                pos=self.dico_live.fit_event3D(intensity,self.pos3D)
                self.fit3d.setData(pos=pos,color=pg.glColor((20,20)), width=5)  # charge les donnees de la droite 
            if(self.option_num!=1):
                self.fit3d.setData(pos=np.array([0,0,0]),color=pg.glColor((20,30)), width=5)
            self.ui.plt3d.items=self.view3d.w.items
        
        # update of the angle histogram
        self.y,self.x=np.histogram(self.theta,bins=np.linspace(-90, 90, 36))   # data histogram
        self.Hist.setData(self.x,self.y,stepMode=True, fillLevel=0, brush=(0, 0, 255, 80)) # send data angle histogram
        
        if self.calibrate_MIP and self.calib_events%10 :
            with open(self.path_calib,"w") as csvsavedfile:
                writerdata=csv.writer(csvsavedfile,delimiter='\t',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writerdata.writerows(self.mip_calibration)
        
        self.acq_proc.last_event_plotted = self.acq_proc.evNumber.get_partial()[0]     # mark this event as already plotted and waits for the next event
        
        self.Auto.set_data(self.Hist,self.FreqHist,self.scatt,self.droite)
        
        #input("Waiting that you click")
    
    def integrate(self,intensity) :
        
        self.int_events += 1
        int_intensity = []
        
        if len(self.int_intensities) == 0 :
            self.int_intensities = intensity[:]
            return intensity
        
        for i, pi in zip(intensity,self.int_intensities) :
            newint = ( (self.int_events -1) * pi + i) / self.int_events
            int_intensity.append( newint )
            
        self.int_intensities = int_intensity
        
        return np.array(int_intensity)*10.

    def calibrate(self,intensity) : # intensity is data here !
        self.calib_events += 1
        if len(self.mip_calibration) == 0 :
            for ni in intensity :
                 if ni > 0 : self.mip_calibration.append( (ni, 1) )
                 else : self.mip_calibration.append( (0, 0) )
            return
            
        newcalib = []    
        for ni,i in zip(intensity,self.mip_calibration) :
            intens, nevts = i
            if ni > 0 : newcalib.append( ( (nevts*intens + ni)/(nevts+1), nevts+1 ) )
            else : newcalib.append(i)
                    
        self.mip_calibration = newcalib

    def load_calibration(self) :
        if os.path.exists(self.path_calib):
            self.mip_calibration = [x[0] for x in np.genfromtxt(self.path_calib)]

        # CLASSIFY EACH DATA ON A DICTIONNARY
    def fill_dico(self):      # class data for each click
        self.acq_proc.fetch_data() # get data from pipe
        current_pos=self.acq_proc.data.curr_pos # current position
        if(self.acq_proc.data.curr_pos!=0 and current_pos!=self.sp): # avoid copy
            self.sp=current_pos
            
            data=self.acq_proc.plot_signals_map()   # give process data in p.e or MIP (without noise)
            
            ## Trigger implementation
            self.trigger_dec = True
            if self.trigger_type in triggers : 
                self.trigger_dec = triggers[self.trigger_type](self.acq_proc.make_data_grid(data), layers = 5)
                if not self.trigger_dec : return
            ## continuing what was there before
            
            ## Frequqncy plot
            nt = time.time() - self.start_time
            if len(self.tsampled) == 0 :
                self.tsampled.append( nt )
                self.vsampled["nevt"].append( self.acq_proc.Class_EventLive['AllEvents'].len() )
                self.vsampled["freq"].append( ( 0., 0. ) )
                
            dt = nt - self.tsampled[-1]
            if dt > self.sample_dt :
                dn = self.acq_proc.Class_EventLive['AllEvents'].len() - self.vsampled["nevt"][-1]
                self.tsampled.append( nt )
                self.vsampled["nevt"].append( self.acq_proc.Class_EventLive['AllEvents'].len() )
                
                ## Only for dn > 0 to avoid negative frequencies when time resets
                if dn > 0 : self.vsampled["freq"].append( ( nt, float(dn) / dt ) )
            
            self.acq_proc.Class_EventLive = self.dico_live.classify_event(data,self.acq_proc.evNumber.get_partial())# fill dico
            self.energie_tot_seperete=self.dico_live.energie_deposite_seperete()  # event's energie 
            self.event_seperete=self.dico_live.event_id() # event's id 
            
            if self.dico_live.last_event_type == "Muon":
                slope = None
                if "m" in self.dico_live.fit_results : slope = self.dico_live.fit_results['m']
                #print("slope=",slope)
                if slope :
                    self.theta.append(math.atan(-1./(slope*self.slope_conversion_factor)))   # this is the right theat angle, the one measured with real coordinates
                    #self.theta.append(self.dico_live.fit_results['theta'])  # this is not the true theta (in terms of real coordinates)! Need to correct for that!
                    #print("true theta=",self.theta)
                else :
                    self.theta.append(0.)
                if self.calibrate_MIP : self.calibrate(data)                                                    # plot fit
            
            self.FreqHist.setData(
                [x[0] for x in self.vsampled["freq"]],
                [x[1] for x in self.vsampled["freq"]],
                stepMode=False, fillLevel=0, brush=(0, 0, 255, 80)) # send data angle histogram
            
            self.nb_events_per_class=[self.acq_proc.Class_EventLive['AllEvents'].len(),self.acq_proc.Class_EventLive['Muon'].len(),  # signal per categorie 
                                self.acq_proc.Class_EventLive['Electron'].len(),self.acq_proc.Class_EventLive['Disintegration'].len(),self.acq_proc.Class_EventLive['HighEnergyElectron'].len()]
            print(self.acq_proc.Class_EventLive['AllEvents'].len())
            for event,nbr in enumerate(self.nb_events_per_class):   # saved when buffer is full
                if(nbr==self.acq_proc.num_integrations):
                    key=self.event_name[event]
                    self.nbr_saving[event]+=1
                    self.acq_proc.backup_dico_csv(self.path_backupdico,key,save='save')
     
    def state_plotAll(self):
        self.acq_proc.option='AllEvents'  # 0
        self.option_num=0
        if(self.acq_proc.Class_EventLive['AllEvents'].len()!=0):
            self.timer_plot_update.singleShot(2,self.update_plot)
    def state_plotMuon(self):
        self.acq_proc.option='Muon'   # 1
        self.option_num=1
        if(self.acq_proc.Class_EventLive['Muon'].len()!=0):
            self.timer_plot_update.singleShot(2,self.update_plot)
    def state_plotElectron(self):
        self.acq_proc.option='Electron'  # 2
        self.option_num=2
        if(self.acq_proc.Class_EventLive['Electron'].len()!=0):
            self.timer_plot_update.singleShot(2,self.update_plot)
    def state_plotDisintegration(self):
        self.acq_proc.option='Disintegration'  # 3
        self.option_num=3
        if(self.acq_proc.Class_EventLive['Disintegration'].len()!=0):
            self.timer_plot_update.singleShot(2,self.update_plot)
    def state_plotHighEnergyElectron(self):
        self.acq_proc.option='HighEnergyElectron'  # 4
        self.option_num=4
        if(self.acq_proc.Class_EventLive['HighEnergyElectron'].len()!=0):
            self.timer_plot_update.singleShot(2,self.update_plot)
            
    def rotation(self):
        if(self.play_cam==0):
            self.view3d.timer_camera(0)
            self.view3d.timer_cam.start()
            self.play_cam=1
        else:
            self.view3d.timer_camera(0.2)
            self.view3d.timer_cam.start()
            self.play_cam=0
        
        ## draw sensors on 2d plot
    def module_2D(self):
        sensor=np.array([self.acq_proc.x_coords,self.acq_proc.y_coords])
        x=0.4;y=0.2
        for i in range(len(self.acq_proc.x_coords)):
            pos=np.array([[sensor[0][i]-x,sensor[1][i]-y],[sensor[0][i]-x,sensor[1][i]+y],[sensor[0][i]+x,sensor[1][i]-y],[sensor[0][i]+x,sensor[1][i]+y]])
            lines = np.array([
                (25.5,127.5,127.5,200,2),
                (25.5,127.5,127.5,200,2),
                (25.5,127.5,127.5,200,2),
                (25.5,127.5,127.5,200,2)]
                , dtype=[('red',np.ubyte),('green',np.ubyte),('blue',np.ubyte),('alpha',np.ubyte),('width',float)])
            adj=np.array([[0,1],[1,3],[3,2],[2,0]])
            self.module[i]=pg.GraphItem(pos=pos,adj=adj,pen=lines,size=1,pxMode=True)
            self.tracker.addItem(self.module[i])
    
    # draws Pb plates
    def plates_Pb(self):
        
        # set Pb plates coordinates
        sorted_x =np.unique(self.acq_proc.x_coords)
        x_middle = 0.5*(sorted_x[-1] + sorted_x[0])   # same x position for all plates
        y_middle = []   # y positions (between the stations)
        sorted_y = np.unique(self.acq_proc.y_coords)
        y_middle.append(0.5*(sorted_y[3] + sorted_y[2]))
        y_middle.append(0.5*(sorted_y[4] + sorted_y[3]))
        y_middle.append(0.5*(sorted_y[5] + sorted_y[4]))
        y_middle.append(0.5*(sorted_y[6] + sorted_y[5]))
        y_middle.append(0.5*(sorted_y[7] + sorted_y[6]))
        
        x_width = (30*1)/3      # 30 cm wide
        y_width = (0.5*1)/10    # 0.5 cm thick
        
        for i,y_mid in enumerate(y_middle):
            self.pb_plates[i] = pg.QtGui.QGraphicsRectItem(x_middle-0.5*x_width, y_mid-0.5*y_width, x_width, y_width)
            self.pb_plates[i].setBrush(pg.mkBrush('c'))
            self.tracker.addItem(self.pb_plates[i])
            
class CommandWindow(QtGui.QMainWindow):
    def __init__(self,acq):
        QtGui.QMainWindow.__init__(self)
        
        self.USBBoard_filename = "test"     # USBboard filename without ".root"
        self.USBboard_Nevents = 100000      # Number of events to take with USBboard before closing the file (and quiting acquisition)
        self.USBboard_filecounter = 0       # file number : filename = USBBoard_filename + USBboard_filecounter + ".root"
        self.USBboard_filepath = "/home/lphe/scifi-data/vata64-data/TrackerDemo/"   # path to where to save USBboard root files (from ecalTest)
        
        self.ui = Ui_CommandWindow()
        self.ui.setupUi(self)     
        self.acq_proc=acq               # obj DAQ
        self.main=LiveWindow(acq)       # window live
        self.Display=SavedWindow(acq)   # window saved
        self.Poster=PosterWindow()      # window poster

        #Constante
        self.savedrun=False
        self.liverun=False
        self.frequency=100    # timer frequency
        #Configuration
        self.sig_load_setup_file()  # initialize pedestals and gains
        self.sig_load_sensor_pos()    # innitialize geometri sensor
        self.configure_signal()        # initialize interface
        self.data_load()               # load data file wanted to read
        self.configure_dico(0)     # 
        self.configure_timer()
        self.main.state_plotAll()
        self.main.configure_timers()
        self.Display.configure_timers()
        self.Display.state_plotAll()
        self.configure_data_csv()
        self.configure_classify_csv() 
        self.get_value_USB_board()
        self.get_file_USB_board()
        
        self.main.module_2D() 
        self.main.plates_Pb()
        self.Display.module_2D()
        self.main.view3d.module([0.8,10,1/4])
        self.Display.view3d.module([0.8,10,1/4])
        #LOGO
        self.ui.label_logo.setPixmap(QtGui.QPixmap('/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/detector.jpg'))
        
        self.main.setRange2Dplot()
        
    def configure_timer(self):
        self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(self.display_values)
        self.timer.start(50)
        
    def configure_signal(self):
        #LIVE BUTTONS
        self.ui.pushButton_LIVE.clicked.connect(self.live)
        self.ui.btnLiveStart.clicked.connect(self.live_start)
        self.ui.btnLivePause.clicked.connect(self.live_pause)
        self.ui.btnLiveLeft.clicked.connect(self.do_left)
        self.ui.btnLiveRight.clicked.connect(self.do_right)
        self.ui.btnLiveStopacq.clicked.connect(self.stop_daq)
        self.ui.radioButton_muon.clicked.connect(self.main.state_plotMuon)
        self.ui.radioButton_electron.clicked.connect(self.main.state_plotElectron)
        self.ui.radioButton_disintegration.clicked.connect(self.main.state_plotDisintegration)
        self.ui.radioButton_highelectron.clicked.connect(self.main.state_plotHighEnergyElectron)
        self.ui.radioButton_All.clicked.connect(self.main.state_plotAll)
        self.ui.integration_bt.clicked.connect(self.switch_integration)
        self.ui.automatic_bt.clicked.connect(self.switch_automatic)
       
        #3D setup
        self.ui.rotation.clicked.connect(self.main.rotation)
        self.ui.rotation_saved.clicked.connect(self.Display.rotation)
        #SAVED BUTTONS
        self.ui.pushButton_SavedData.clicked.connect(self.saved_data)
        self.ui.btnSavedStart.clicked.connect(self.saved_start)
        self.ui.btnSavedRight.clicked.connect(self.saved_doright)
        self.ui.btnSavedPause.clicked.connect(self.saved_pause)
        self.ui.btnSavedLeft.clicked.connect(self.saved_doleft)
        self.ui.spinBox_Event.valueChanged.connect(self.go_event)
        self.ui.radioButton_muon_sd.clicked.connect(self.Display.state_plotMuon)
        self.ui.radioButton_electron_sd.clicked.connect(self.Display.state_plotElectron)
        self.ui.radioButton_disintegration_sd.clicked.connect(self.Display.state_plotDisintegration)
        self.ui.radioButton_highelectron_sd.clicked.connect(self.Display.state_plotHighEnergyElectron)
        self.ui.radioButton_All_sd.clicked.connect(self.Display.state_plotAll)
        #PARAMETERS BUTTON
        self.ui.spinBox_Acq.valueChanged.connect(self.change_buffer_size)
        self.ui.DataLoadbtn.clicked.connect(self.data_load)
        self.ui.sensorLoadbtn.clicked.connect(self.load_sensor_pos)
        self.ui.setupLoadbtn.clicked.connect(self.load_setup_file)
        self.ui.load_save_as.clicked.connect(self.configure_data_csv)
        self.ui.load_save_classify_data.clicked.connect(self.configure_classify_csv)
        self.ui.load_USB_board_file.clicked.connect(self.get_file_USB_board)
        self.ui.spinBox_USB_board.valueChanged.connect(self.get_value_USB_board)
        #POSTER
        self.ui.poster.clicked.connect(self.poster)
    
    def switch_integration(self) :
        self.main.integrate_on = not self.main.integrate_on
        print ("Integration mode ON --> ",self.main.integrate_on)
    
    def switch_automatic(self) :
        self.live()
        #while True :
        #    
        #    print ("INWHILE")
        #    i, o, e = select.select( [sys.stdin], [], [], 10 )
        #    if i : break
            
            
    
        # unused
    def change_buffer_size(self):
        self.acq_proc.num_integrations=self.ui.spinBox_Acq.value()
        self.acq_proc.reset_buffers()
        self.acq_proc.reset_event_classification_live()   
        self.configure_dico(1)
        log.info("buffersize change to {}".format(self.acq_proc.num_integrations))
    
    ## CONFIGURATIONS DES DICTIONNAIRES 
    def configure_dico(self,key=0): 
        if(key==0):
            self.main.dico_live=Classify(self.acq_proc.Class_EventLive,self.ui.lineEdit_SensorPos.text(),self.ui.lineEdit_SetupFile.text())
            self.Display.dico_saved=Classify(self.acq_proc.Class_EventSaved,self.ui.lineEdit_SensorPos.text(),self.ui.lineEdit_SetupFile.text())
        if(key==1):
            self.main.dico_live=Classify(self.acq_proc.Class_EventLive,self.ui.lineEdit_SensorPos.text(),self.ui.lineEdit_SetupFile.text())
        if(key==2):
            self.Display.dico_saved=Classify(self.acq_proc.Class_EventSaved,self.ui.lineEdit_SensorPos.text(),self.ui.lineEdit_SetupFile.text())
    ### FICHIERS D'ENREGISTREMENT DES DONNEES
    def configure_data_csv(self):                                  
        path_backupfile=self.ui.lineEdit_SaveAs.text()
        self.acq_proc.backup_csv(path_backupfile,'config')
        log.info("Data saved in {}".format(path_backupfile)) 
    
    def configure_classify_csv(self):
        self.main.path_backupdico=self.ui.lineEdit_Dossier.text()
        self.acq_proc.backup_dico_csv(self.main.path_backupdico,save='config')
        log.info("Data Classify saved in {}".format(self.main.path_backupdico))  

    ## LOAD fICHIERS SETUP ET GEOMETRIE 
    def sig_load_setup_file(self):
        file_path = self.ui.lineEdit_SetupFile.text()
        self.acq_proc.load_general_setup_file(file_path)
        self.configure_dico()

    def sig_load_sensor_pos(self):
        file_path = self.ui.lineEdit_SensorPos.text()
        log.info("Loading sensor description file {}".format(file_path))
        data = np.genfromtxt(file_path, dtype=np.float)
        # Format is: x,y,sensor_num
        #print(data)
        self.acq_proc.set_sensor_pos(data[:,5], data[:,4], data[:,0], data[:,1])
        
    def get_value_USB_board(self):
        self.USBboard_Nevents=self.ui.spinBox_USB_board.value()
    
    def get_file_USB_board(self):
        self.USBboard_filename=self.ui.USB_board_file.text()

    def load_sensor_pos(self):
        self.stop_daq()
        self.clear()
        file_path = self.ui.lineEdit_SensorPos.text()
        log.info("Loading sensor description file {}".format(file_path))
        data = np.genfromtxt(file_path, dtype=np.float)
        # set sensor position (as unit, we have channel number as y and layer number as z)
        self.acq_proc.set_sensor_pos(data[:,5], data[:,4], data[:,0], data[:,1])
        self.main.module_2D() 
        self.Display.module_2D()
        self.main.view3d.module([0.8,10,1/4])
        self.Display.view3d.module([0.8,10,1/4])
        self.configure_dico()
        # conversion factor between slope and angle in 2D plot and in reality (=true geometry)
        # here a simple implementation enough for now
        x = np.unique(data[:,5])
        xprime = np.unique(data[:,2])
        xconv = (xprime[-1]-xprime[0])/(x[-1]-x[0])
        y = np.unique(data[:,4])
        yprime = np.unique(data[:,3])
        yconv = (yprime[-1]-yprime[0])/(y[-1]-y[0])
        self.main.slope_conversion_factor = yconv/xconv
    
    def load_setup_file(self):
        self.stop_daq()
        file_path = self.ui.lineEdit_SetupFile.text()
        self.acq_proc.load_general_setup_file(file_path)
        self.configure_dico()
    
    def clear(self):
        if(len(self.main.view3d.w.items)>5):
            for i in range(len(self.acq_proc.x_coords)):
                self.main.tracker.removeItem(self.main.module[i])
                self.Display.plot2.removeItem(self.Display.module[i])
                self.main.view3d.w.removeItem(self.main.view3d.barette[i])
                self.Display.view3d.w.removeItem(self.Display.view3d.barette[i])

    ## DISPLAY VALUE ON COMMAND WINDOW
    def display_values(self):                                ##### affiche le nombre d'event dans chaque catégorie
        self.ui.ALL_Ind.display(self.main.nb_events_per_class[0]+self.acq_proc.num_integrations*self.main.nbr_saving[0])
        self.ui.electron_Ind.display(self.main.nb_events_per_class[2]+self.acq_proc.num_integrations*self.main.nbr_saving[2])
        self.ui.muon_Ind.display(self.main.nb_events_per_class[1]+self.acq_proc.num_integrations*self.main.nbr_saving[1])
        self.ui.disintegration_Ind.display(self.main.nb_events_per_class[3]+self.acq_proc.num_integrations*self.main.nbr_saving[3])
        self.ui.highelectron_Ind.display(self.main.nb_events_per_class[4]+self.acq_proc.num_integrations*self.main.nbr_saving[4])
        self.ui.ALL_Ind_sd.display(self.Display.nb_events_per_class[0])
        self.ui.electron_Ind_sd.display(self.Display.nb_events_per_class[2])
        self.ui.muon_Ind_sd.display(self.Display.nb_events_per_class[1])
        self.ui.disintegration_Ind_sd.display(self.Display.nb_events_per_class[3])
        self.ui.highelectron_Ind_sd.display(self.Display.nb_events_per_class[4])
        if(self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].len()!=0):
            self.ui.current_event.display(self.Display.event_seperete[self.Display.option_num][self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].free_pos])
            self.Display.ui.EnergieDep.setText(str(self.Display.energie_tot_seperete[self.Display.option_num][self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].free_pos])+" MIP")
        if(self.acq_proc.Class_EventLive[self.acq_proc.option].len()!=0):
            if(self.acq_proc.lastpos==True):
                self.ui.CurrentEven.display(self.main.event_seperete[self.main.option_num][self.acq_proc.Class_EventLive[self.acq_proc.option].curr_pos-1
                                                +self.acq_proc.num_integrations*self.main.nbr_saving[self.main.option_num]])
                self.main.ui.EnergieDep.setText(str(self.main.energie_tot_seperete[self.main.option_num][self.acq_proc.Class_EventLive[self.acq_proc.option].curr_pos-1
                                               +self.acq_proc.num_integrations*self.main.nbr_saving[self.main.option_num]])+" MIP")
                self.main.ui.EventType.setText(self.main.event_type)
            else:
                self.ui.CurrentEven.display(self.main.event_seperete[self.main.option_num][self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos
                                                    +self.acq_proc.num_integrations*self.main.nbr_saving[self.main.option_num]])
                self.main.ui.EnergieDep.setText(str(self.main.energie_tot_seperete[self.main.option_num][self.acq_proc.Class_EventLive[self.acq_proc.option].free_pos
                                               +self.acq_proc.num_integrations*self.main.nbr_saving[self.main.option_num]])+" MIP")
                self.main.ui.EventType.setText(self.main.event_type)

   # def message_error(self):
        
    ######## LIVE ##########
    # START ACQUISITION    
    def live(self):
        log.info("Start DAQ")
        options=[]
        
        #-------------- Selection of subprocess to be launched --------------
        #------ Faking PEBS DAQ
        #cmd="./fake_track_pebs.py"
        
        #------ USBBoard true DAQ: for single DAQ -> generating only one ROOT file and then terminate
        cmd="/home/lphe/usbBoard/Builds/tracker_demo_daq.sh"
        fullname=str(self.USBboard_filepath)+str(self.USBboard_filename)+str(self.USBboard_filecounter)+".root"
        options=[fullname, str(self.USBboard_Nevents)]
        
        #------ USBBoard true DAQ: for multiple DAQ -> generating ROOT file with Nevents and then restarting (with an increment in the filename)
        #cmd="/home/lphe/usbBoard/Builds/tracker_demo_daq_multiple.sh"
        #options=[str(self.USBboard_filepath), str(self.USBboard_filename), str(self.USBboard_Nevents)]
        
        #------ Faking TRACKERDEMO DAQ
        #cmd="./fake_track_TrackerDemo.py"
        
        #--------------------------------------------------------------------
        
        self.acq_proc.start_acquisition(cmd,options)
        self.liverun=True
        self.main.live_mode = True
        self.acq_proc.lastpos=True
        self.main.timer_acquisition.start(self.frequency)
        self.main.timer_plot_update.start(self.frequency)
        self.main.show()
    
    # DISPLAY PAUSE
    def live_pause(self):
        self.main.live_mode = False
        self.main.timer_plot_update.stop()
        self.main.show()   
    
    # DISPLAY START  display the last data
    def live_start(self):
        self.acq_proc.lastpos=True
        self.liverun=True
        self.main.live_mode = True
        self.main.timer_plot_update.start(self.frequency)
    
    # STOP DAQ
    def stop_daq(self):
        log.info("Stop DAQ")
        self.acq_proc.stop_acquisition()
        self.main.timer_acquisition.stop()
        self.main.timer_plot_update.stop()
        self.acq_proc.reset_buffers()
    
    # dislay the left trace
    def do_left(self):
        if(self.liverun==True):
            self.live_pause()
        self.acq_proc.lastpos=False
        self.main.timer(cmd="left")
        self.main.timer_plot_update.singleShot(2,self.main.update_plot)
        self.main.show()
    
    # display right trace    
    def do_right(self):
        if(self.liverun==True):
            self.live_pause()
        self.acq_proc.lastpos=False
        self.main.timer(cmd="right")
        self.main.timer_plot_update.singleShot(2,self.main.update_plot)
        self.main.show()
    
    ####### SAVED ###########
    # DISPLAY PAUSE
    def saved_pause(self):
        self.Display.timer_plot_update.stop()
        self.Display.show()
    
    #DISPLAY START    display successive data
    def saved_start(self):
        if(self.Display.ip==True):
            log.info("Data end")
            self.saved_pause()
        else: 
            self.Display.timer_plot_update.start(500)
            self.savedrun=True
        self.Display.show()
    
    #display the left trace
    def saved_doleft(self):
        if(self.savedrun==True):
            self.saved_pause()
            self.savedrun=False
        self.Display.timer(cmd="left")
        self.Display.timer_plot_update.singleShot(2,self.Display.upd_plt)
        self.Display.show()
    
    #display the right trace
    def saved_doright(self):
        if(self.savedrun==True):
            self.saved_pause()
            self.savedrun=False
        self.Display.timer(cmd="right")
        self.Display.timer_plot_update.singleShot(2,self.Display.upd_plt)
        self.Display.show()
    
    # go to the id trace selected
    def go_event(self):
        num_event = self.ui.spinBox_Event.value()
        if(0<=num_event<self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].len()):
            self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].free_pos=num_event-1
            self.Display.timer_plot_update.singleShot(2,self.Display.upd_plt)
        else:log.info("Event request out of range")
        self.Display.show()
    
    # LOAD DATA FROM A FILE
    def data_load(self):
        path = self.ui.lineEdit_DataPath.text()
        log.info("Loading Data file {} WAIT...".format(path))
        ns=time.time()
        self.Display.datafile = np.genfromtxt(path)    # prend 8s 
        ne=time.time()
        log.info("Loading time {}".format(ne-ns))
        self.savedrun=False
        if(self.Display.datafile[1:]=="nan"):
            log.info("Loading failed")
        self.acq_proc.reset_event_classification_saved(len(self.Display.datafile))
        self.configure_dico(2)
        
    # CLASSIFY DATA LOADED
    def saved_data(self):
        if(self.savedrun==False):
            self.Display.trier()
        self.savedrun=True
        self.Display.show()
    
    # SHOW POSTER WINDOW
    def poster(self):
        self.Poster.show()
        
    # CLOSE SOFTWARE
    def closeEvent(self, event):
        print('Window closed: ')
        print('event: {0}'.format(event))
        if self.acq_proc.sp is not None:
            if self.acq_proc.sp.proc:
                self.acq_proc.sp.proc.terminate()
        #time.sleep(5)
        self.Display.timer_plot_update.stop()
        self.main.timer_plot_update.stop()
        self.main.timer_acquisition.stop()
        self.timer.stop()
        win2.close()
        win3.close()
        # et ici tout ce qu'il faut potentiellement faire pour quitter comme il faut.
        event.accept()


class PosterWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui=Ui_PosterWindow()
        self.ui.setupUi(self)
        self.ui.cosmicray.setPixmap(QtGui.QPixmap("/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/image_cosmicray.jpg"))
        self.ui.track_muon.setPixmap(QtGui.QPixmap("/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/muon.png"))
        self.ui.track_electron.setPixmap(QtGui.QPixmap("/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/electron.png"))
        self.ui.schema.setPixmap(QtGui.QPixmap("/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/schemacosmicray.jpg"))
        self.ui.detector.setPixmap(QtGui.QPixmap("/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/detector.png"))
        self.ui.signal.setPixmap(QtGui.QPixmap("/home/lphe/cosmic_analysis/python-scripts/RTGraph/src/img/signal.png"))
        
        
        
class SavedWindow(QtGui.QMainWindow):
    def __init__(self,acq_proc):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_DisplayModeWindow()
        self.ui.setupUi(self)
        
        self.acq_proc=acq_proc  # daq object
        self.view3d=View3D(self.ui.plt3d,acq_proc)     #object 3d
        
        self.cmd=None  # command path
        self.ip=True    # booleen
        self.nb_events_per_class=[0]*5     
        self.energie_tot_seperete=[[0]]*5  
        self.theta=[]        # array of each muon trace
        self.event_seperete=[[0]]*5   # array of event id
        self.play_cam=1
        
        self.configure_plot_saved_data()
        
        #CONFIGURATION
    def configure_plot_saved_data(self):
        self.img_cannaux = pg.ImageItem()
        self.scatt=pg.ScatterPlotItem(pxMode=False,pen=pg.mkPen(None))
        self.droite = pg.PlotDataItem(x=[],y=[],pen=pg.mkPen(color=(255, 0, 0),width=3))
        self.Hist=pg.PlotCurveItem()
        self.module=[pg.GraphItem()]*400
        ################### creation des objects d'affichage ########################
        # array used in 3d
        self.pos3D = np.empty((self.acq_proc.num_sensors_enabled, 3))
        self.size3D = np.empty(self.acq_proc.num_sensors_enabled)
        self.color3D = np.empty((self.acq_proc.num_sensors_enabled, 4))
        # Object plot 3D
        self.scat3d = gl.GLScatterPlotItem(pos=self.pos3D, size=self.size3D, color=self.color3D, pxMode=False)
        self.fit3d = gl.GLLinePlotItem(pos=self.pos3D,color=pg.glColor((0,1.3)), width=1, antialias=True)
        self.view3d.w.addItem(self.scat3d)
        self.view3d.w.addItem(self.fit3d)
        # Object graphiques diff plot sont ajouter sur une zone de graphique graphiqueview
        self.plot1 = self.ui.pltchannel.addPlot(title ="Channels")
        self.plot1.addItem(self.img_cannaux )
        self.plot2=self.ui.plttracker.addPlot(title='Tracker')
        self.plot2.addItem(self.scatt)
        self.plot2.addItem(self.droite)
        self.plot3=self.ui.plthisto.addPlot(title='Angle incidencie')
        self.plot3.addItem(self.Hist)
        self.plot4=self.ui.pltfrequency.addPlot(title='Event frequency')
        
        
    def configure_timers(self):     
        self.timer_plot_update = QtCore.QTimer(self)
        self.timer_plot_update.timeout.connect(self.timer)
        self.timer_plot_update.timeout.connect(self.upd_plt)
    
        # TIMER select the trace for each click
    def timer(self,cmd="right"):     
        if(cmd=="left" and self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].free_pos>0 ):
            self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].free_pos-=1
        if(cmd=="right" and self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].free_pos<self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].len()-1):
            self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].free_pos+=1
        if(self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].free_pos==self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].len()-1):
            self.timer_plot_update.stop()
            self.ip=True
        else:self.ip=False
        
        #STATE OF DISPLAY MODE (MUON OR ELECTRON...) 
    def state_plotAll(self):
        self.acq_proc.option_saved='AllEvents'
        self.option_num=0
        self.timer_plot_update.singleShot(2,self.upd_plt)
    def state_plotMuon(self):
        self.acq_proc.option_saved='Muon'
        self.option_num=1
        self.timer_plot_update.singleShot(2,self.upd_plt)
    def state_plotElectron(self):
        self.acq_proc.option_saved='Electron'
        self.option_num=2
        self.timer_plot_update.singleShot(2,self.upd_plt)
    def state_plotDisintegration(self):
        self.acq_proc.option_saved='Disintegration'
        self.option_num=3
        self.timer_plot_update.singleShot(2,self.upd_plt)
    def state_plotHighEnergyElectron(self):
        self.acq_proc.option_saved='HighEnergyElectron'  
        self.option_num=4
        self.timer_plot_update.singleShot(2,self.upd_plt)
    
        #SCATTER PLOT give array to plot the scatter dimension array: size=sensor number (320,128...)
    def plot_signals_scatter(self): 
        current_pos=self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].free_pos
        colors=[]
        data = self.acq_proc.Class_EventSaved[self.acq_proc.option_saved][current_pos]
        if(len(data)!=len(self.acq_proc.sensor_ids)):
            log.warning("The geometry file don't fit with data length")
            self.timer_plot_update.stop()
            return False
        #intensity = data[self.acq_proc.sensor_ids] 
        intensity = data
        maxintensity = np.max(intensity)
        for i in range(len(self.acq_proc.sensor_ids)):
             intensity[i]=math.log(intensity[i]+1)
             colors.append(pg.intColor(2+intensity[i], hues=(100/self.acq_proc.PetoMip)*1, values=1, maxValue=255, minValue=150, maxHue=360, minHue=0, sat=255, alpha=255)) 
        return intensity, colors, maxintensity,data
    
        # PROCESS DATA      give data in photoelectron or in MIP 
    def plot_signals_map(self):
        data=self.acq_proc.data_load.get_partial()
        event=data[0]
        data=data[2:]  # retire le num de l'event et le temps
        pedestals=self.acq_proc.calibration_all_channels['pedestals']   # array de pedestal= electronical noise
        gains=self.acq_proc.calibration_all_channels['gains']
        for i in range(len(gains)):                
            if(gains[i]==0):    
                gains[i]=1
                log.warning("Gains are null")
        data=(data[0:self.acq_proc.num_sensors_enabled]-pedestals)/(gains[0:self.acq_proc.num_sensors_enabled]*self.acq_proc.PetoMip)
        for i in range(len(data)):                 
            if(data[i]<0 or data[i]<self.acq_proc.Threshold):                                #retire les donnees en dessous de threshold
                data[i]=0
        return data,event 
        
        # UPDATE PLOT
    def upd_plt(self):                # fonction plot, generer par timer
        if(self.plot_signals_scatter()==False):
            self.timer_plot_update.stop()
        else:
            intensity, colors, maxintensity,data = self.plot_signals_scatter()                # donnee du plots 
            self.y,self.x=np.histogram(self.theta,bins=np.linspace(-50, 50, 20))               
            # histogramme angles
            self.Hist.setData(self.x,self.y,stepMode=True, fillLevel=0, brush=(0, 0, 255, 80))
            # histogramme cannaux 
            self.img_cannaux.setImage(data.reshape(self.acq_proc.num_sensors_enabled,1))     
            if(maxintensity!=0):
            # plot le scatterplot
                self.scatt.setData(x=self.acq_proc.x_coords,                                  
                                y=self.acq_proc.y_coords,size=(intensity/5),brush=colors)
            if(self.acq_proc.option_saved=='Muon'):
                x,y=self.dico_saved.fit_event(data,plot=True)
                 # trace la droite de fit
                self.droite.setData(x,y)                                                      
            else:self.droite.setData([0],[0])
            ##### 3D #####
            # the third dimension is calculated with random
            y,z,x_coord=self.dico_saved.signal_xyz(intensity)                # give coordonee(x_coord,y,z), signal in MIP or p.e and two points(verts) to plot fiting muon trace
            x_coords=self.dico_saved.simulation_x(intensity)
            for i in range(len(self.acq_proc.y_coords)):
                self.color3D[i]=(1,1,1,1)                   # color array
            #self.pos3D=np.vstack([x_coord,y,z]).transpose()  # array contenant les donnees 3d 
            self.pos3D=np.vstack([x_coords,-self.acq_proc.Sensor_per_Stage/2+self.acq_proc.x_coords,-self.acq_proc.nb_Stage/2 + self.acq_proc.y_coords]).transpose()
            if(maxintensity!=0):
                self.scat3d.setData(pos=self.pos3D,size=np.asarray(intensity)/maxintensity,color=self.color3D) # charge les donnees
            self.view3d.affichage(intensity,x_coords)  # affiche le graph 3d
            if(self.option_num==1):
                pos=self.dico_saved.fit_event3D(intensity,self.pos3D)
                self.fit3d.setData(pos=pos,color=pg.glColor((20,20)), width=5)  # charge les donnees de la droite 
            if(self.option_num!=1):
               self.fit3d.setData(pos=np.array([0,0,0]),color=pg.glColor((20,30)), width=5)
            self.ui.plt3d.items=self.view3d.w.items
    
    def event_display(self):
        self.event_seperete[self.option_num][self.acq_proc.Class_EventSaved[self.acq_proc.option_saved].free_pos]
         
        #    SEPERATE DATA IN A DICTIONNARY                     
    def trier(self):
        for i,data in enumerate(self.datafile):
            self.acq_proc.data_load.append(data[0:self.acq_proc.num_sensors_enabled+2])
            self.dataPlot,event=self.plot_signals_map()
            self.acq_proc.Event_id_Saved.append(event)
            self.acq_proc.Class_EventSaved,self.theta = self.dico_saved.classify_event(self.dataPlot,self.acq_proc.Event_id_Saved.get_partial())
            self.energie_tot_seperete=self.dico_saved.energie_deposite_seperete()
            self.event_seperete=self.dico_saved.event_id()
        self.nb_events_per_class=[self.acq_proc.Class_EventSaved['AllEvents'].len(),self.acq_proc.Class_EventSaved['Muon'].len(),
                                        self.acq_proc.Class_EventSaved['Electron'].len(),self.acq_proc.Class_EventSaved['Disintegration'].len(),self.acq_proc.Class_EventSaved['HighEnergyElectron'].len()]                                 

    def rotation(self):   # rotation camera
        if(self.play_cam==0):
            self.view3d.timer_camera(0)
            self.view3d.timer_cam.start()
            self.play_cam=1
        else:
            self.view3d.timer_camera(0.2)
            self.view3d.timer_cam.start()
            self.play_cam=0
            
            ## draw sensors on 2d plot
    def module_2D(self):
        sensor=np.array([self.acq_proc.x_coords,self.acq_proc.y_coords])
        x=0.4;y=0.2
        for i in range(len(self.acq_proc.x_coords)):
            pos=np.array([[sensor[0][i]-x,sensor[1][i]-y],[sensor[0][i]-x,sensor[1][i]+y],[sensor[0][i]+x,sensor[1][i]-y],[sensor[0][i]+x,sensor[1][i]+y]])
            lines = np.array([
                (25.5,127.5,127.5,200,2),
                (25.5,127.5,127.5,200,2),
                (25.5,127.5,127.5,200,2),
                (25.5,127.5,127.5,200,2)]
                , dtype=[('red',np.ubyte),('green',np.ubyte),('blue',np.ubyte),('alpha',np.ubyte),('width',float)])
            adj=np.array([[0,1],[1,3],[3,2],[2,0]])
            self.module[i]=pg.GraphItem(pos=pos,adj=adj,pen=lines,size=1,pxMode=True)
            self.plot2.addItem(self.module[i])
    
def start_logging(level):
    log_format = log.Formatter('%(asctime)s,%(levelname)s,%(message)s')
    logger = log.getLogger()
    logger.setLevel(level)

    file_handler = logging.handlers.RotatingFileHandler("RTGraph.log", maxBytes=(10240 * 5), backupCount=2)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    console_handler = log.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)


def user_info():
    log.info("Platform: %s", platform.platform())
    log.info("Path: %s", sys.path[0])
    log.info("Python: %s", sys.version[0:5])


def man():
    parser = argparse.ArgumentParser(description='RTGraph\nA real time plotting and logging application')
    parser.add_argument("-l", "--log",
                        dest="logLevel",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help="Set the logging level")
    return parser


if __name__ == '__main__':
    multiprocessing.freeze_support()
    args = man().parse_args()
    if args.logLevel:
        start_logging(args.logLevel)
    else:
        start_logging(log.INFO)
    user_info()

    log.info("Starting RTGraph")
    
    # instance of acquisiton/processing stuff:
    ap = AcqProcessing()

    app = QtGui.QApplication(sys.argv)
    win1 = CommandWindow(ap)
    win1.setWindowTitle('Control Window')
    win2 = LiveWindow(ap)
    win2.setWindowTitle('Live Window')
    win3 = SavedWindow(ap)
    win3.setWindowTitle('Saved Window')
    
    win1.show()
    app.exec()

    log.info("Finishing RTGraph\n")
    log.shutdown()
    win1.close()
    win2.close()
    win3.close()
    app.exit()
    sys.exit()
    
