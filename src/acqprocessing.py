import multiprocessing
import numpy as np
import logging as log
import pyqtgraph as pg
import yaml
import itertools
import pickle
import csv 
import math as m

from ringbuffer2d import RingBuffer2D
from pipeprocess import PipeProcess
from multiprocessing import Value
from decimal import Decimal
import time, sys
from triggers import triggers

# AcqProcessing recuperates the data from the acquisition program (here the usbboard software)
# and processes it (= pedestal subtraction, gain per channel etc.) 
# It has therefore loaded all these calibration parameters.
# Due to programmation errors, this class also includes the buffers for the saved events
# which make the program not so clear. But to cut it short, this class hosts all the processed
# data, Live or Saved.
class AcqProcessing:
    def __init__(self):
        # USBBoard data format:
        # ADC data is sent in an array of size
        # size = N_uplinks_per_USB * N_channels_per_uplink
        self.num_sensors = 8*64 # for VATA64 front-end
        self.num_sensors_enabled = 8*64#nbr sensor enable with usbboard 
        self.num_uplinks = 8
        self.num_channels_per_uplinks = 64
        self.MAX_adc = 4095
        self.buffer_size = 100
        self.integrate = False # no integration mode
        self.queue = multiprocessing.Queue()
        self.sp = None # subprocess
        
        self.lastpos=False
        self.option='AllEvents';self.option_saved='AllEvents'
        
        self.uplinks_enabled = None
        self.channels_enabled = None
        self.all_pedestal = 0
        self.all_pedestal_val = 0
        self.path_pedestal_file = ""
        self.all_gain = 0
        self.all_gain_val = 0
        self.path_gain_file = ""
        self.Threshold=0
        self.PetoMip=0
        self.nb_Stage=1
        self.Sensor_per_Stage=0
        #recupère les csv pedestals et gains
        self.calibration_all_channels = dict([('pedestals',np.empty(self.num_sensors_enabled)), ('gains',np.empty(self.num_sensors_enabled))])
        
        self.last_event_plotted = -1
        
        #START DAQ     get data from usb board on the terminal   show pipeprocessing in python
    
    
    #START DAQ
    def start_acquisition(self, cmd, options=[]):
        # Ensure no subprocess is currently running
        if not self.sp:
            self.sp = PipeProcess(self.queue,
                              cmd=cmd,
                              args=options)       
        self.sp.start()
        #time.sleep(1)
        #f = open("myfile","w")
        #oldstdin = sys.stdin
        #sys.stdin = f
        #f.write('amexamex')
        #f.close()
        #sys.stdin = oldstdin
        #print ("Written")
        
    
    #STOP DAQ 
    def stop_acquisition(self):
        if not self.sp:
            self.sp = PipeProcess(self.queue,args=[])
        self.sp.stop()

    ##### SAVE IN CSV####
    def backup_csv(self,path,key=0,ev_Number=0,ts=0):
        #Enregistre les donnees brutes sur un fichier 
        self.path_temp=path
        if(key=='config'):
            newfile=open(self.path_temp,"w")
            newfile.close()
        if(self.data_referenced.len()==self.data_referenced.rows):
            log.info("SAVED DATA")
            with open(self.path_temp,"a") as csvsavedfile:
                writerdata=csv.writer(csvsavedfile,delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writerdata.writerows(self.data_referenced[0:])
            self.reset_buffers()
    
    def backup_dico_csv(self,path,key='AllEvents',save=0):
        self.pathdico_temp=path
        #configuration
        if(save=='config'):
            newfileAll=open(self.pathdico_temp+'AllEvents.csv',"w")
            newfileMuon=open(self.pathdico_temp+'Muon.csv',"w")
            newfileElectron=open(self.pathdico_temp+'Electron.csv',"w")
            newfileDisintegration=open(self.pathdico_temp+'Disintegration.csv',"w")
            newfileAll.close();newfileMuon.close();newfileElectron.close();newfileDisintegration.close()
        #saving
        if(save=='save'):
            for k,i in enumerate(self.Class_EventLive[key]):
                self.data_option.append(i,self.evNumber[k],self.time[k],'addref')
            log.info("SAVED {}".format(key))
            with open(self.pathdico_temp+key+'.csv',"a") as csvsavedfile:
                writerdata=csv.writer(csvsavedfile,delimiter='\t',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writerdata.writerows(self.data_option[0:])
                self.reset_event(key)
    ##############3
    
    # TAKE VALUE FROM PROCESSING
    def parse_queue_item(self, line, save=False):
        # Here retrieve the line pushed to the queue
        # and properly parse it to return 
        # several values such as ID, time, [list of vals]
        line_items = line.split('\t')
        if len(line_items) <= 1: return None, None, None
        items = [int(kk) for kk in line_items]
        ev_num, ts, intensities = items[0], items[1], items[2:]
        #if(self.data.curr_pos==self.data.rows-1):
            #ev_num=ev_num+self.data.rows-1
        if save:
            # all ADC values from USBboard are in intensities
            # takes ADC values selected (channels enabled) with the setup file
            intensities = list(itertools.compress(intensities, self.channels_enabled)) # ceci prend ~5us
            self.data.append(intensities)
            self.data_referenced.append(intensities,ev_num,ts,'addref')
            self.time.append(ts)
            self.evNumber.append(ev_num)
            self.backup_csv(self.path_temp,ev_num,ts)   #### save les donnees non traitees
        return ev_num, ts, intensities
    
    # PROTECTION
    def fetch_data(self):
        # Just for debugging purpose: approx. queue size
        #print("Queue size: {}".format(self.queue.qsize()))
        #kk = 0
        #while not self.queue.empty():
        #    kk+=1
        if not self.queue.empty():
            raw_data = self.queue.get(False)
            self.parse_queue_item(raw_data, save=True)    ###### prend les donnees du terminal 
        #print("Poped {} values".format(kk))
        #if kk == 0: return False
        return True
    
    def getLiveEvent(self):
        event_type = None
        data = None
        if(self.lastpos==True): # LIVE
            # Get live data
            data = self.Class_EventLive[self.option].get_partial()# last value
            self.Class_EventLive[self.option].free_pos=self.Class_EventLive[self.option].curr_pos-1
            # Get event type
            if self.option != "AllEvents":
                event_type = self.option
            else:
                event_type = self.Class_EventLive["AllEventsType"].get_partial()[0]
        else:   # PAUSE
            # Get past data from the ringbuffer2D 
            data = self.Class_EventLive[self.option][self.Class_EventLive[self.option].free_pos]
            # Get event type
            if self.option != "AllEvents":
                event_type = self.option
            else:
                event_type = self.Class_EventLive["AllEventsType"][self.Class_EventLive[self.option].free_pos][0]
        
        return event_type, data
    
    def getSavedEvent(self):
        event_type = None
        data = None
        
        current_pos=self.Class_EventSaved[self.option_saved].free_pos
        data = self.Class_EventSaved[self.option_saved][current_pos]
        if self.option_saved != "AllEvents":
            event_type = self.option_saved
        else:
            event_type = self.Class_EventSaved["AllEventsType"][self.Class_EventSaved[self.option_saved].free_pos][0]
        
        return event_type, data
    
    #SCATTER PLOT 
    def plot_signals_scatter(self,method):
        #renvoie les donnees necessaire au scatter plot
        # les intensités, et les donnees 
        # difference entre data et intensity : intensity is normalized data
        
        event_type, data = method()
        
        if(len(data)!=len(self.sensor_ids)):
            log.warning("The geometry file doesn't fit with data length")
            self.sp.stop()
            return False
        intensity = data/self.calibration_all_channels['normalization']
        
        return intensity, data, event_type
    
    #PROCESS DATA 
    def process_data_correction(self,DATA):   #to apply corrections to live data: DATA=self.data, for saved data: DATA=self.load_data
        # this fonction process data
        #outpout= data-pedes/gain
        if self.integrate:              
            return np.sum(DATA.get_all(), axis=0).reshape(self.num_sensors_enabled,1)
        else:
            data=DATA.get_partial() # last value    get partial donne la dernierre donnee aquise
            pedestals=self.calibration_all_channels['pedestals'] # charge pedestaux   array size nb_sensor
            gains=self.calibration_all_channels['gains']  # charge gain
            
            data = np.asarray([(d-p)/(g*self.PetoMip) for d,p,g in zip(data, pedestals, gains)])
            for i in range(len(data)):                  #retire les donnees en dessous de threshold
                if(data[i]<0 or data[i]<self.Threshold):
                    data[i]=0
            return data.reshape(self.num_sensors_enabled,1)
    
    #TAKE SENSOR POSITION
    def set_sensor_pos(self, x_coords, y_coords, uplink_num, sensor_num):
        self.Sensor_per_Stage=0
        self.nb_Stage=0
        self.x_coords = x_coords
        self.y_coords = y_coords
        sensor_float = (uplink_num%10)*64 + sensor_num
        self.sensor_ids = [int(i) for i in sensor_float]
        y_0=self.y_coords[0]
        x_0=self.x_coords[0]
        #calcul le nb de channels par etage
        for i,x_i in enumerate(self.x_coords):
            self.Sensor_per_Stage+=1    
            if(self.x_coords[i+1]==x_0):
                break
        #calcul le nb d'etage
        for i,y_i in enumerate(self.y_coords):
            if(self.y_coords[i]!=y_0):
                y_0=y_i
                self.nb_Stage+=1
        if np.array_equal(np.sort(sensor_num), np.arange(len(sensor_num))):
            log.warning('Sensors ID not starting at 0, or duplicated, or missing')
        
        
    def set_num_sensors(self, value):
        self.num_sensors = value
    
    def set_integration_mode(self, value):
        self.integrate = value
    
    def make_data_grid(self, data) : 
        
        grid = []
        stage = []
        
        for i,(x,y) in enumerate(zip(self.y_coords,self.x_coords)) :
            if i % self.Sensor_per_Stage == 0 :
                if len(stage) > 0 : grid.append(stage)
                stage = []
            stage.append((data[i],(x,y)))
        grid.append(stage)
        return grid
        
    

####### BUFFERS #################
    def reset_buffers(self):
        self.data = RingBuffer2D(self.buffer_size,           # just data 
                                    cols=self.num_sensors_enabled)
        self.time = RingBuffer2D(self.buffer_size, cols=1) 
        self.evNumber = RingBuffer2D(self.buffer_size, cols=1) 
        self.data_referenced=RingBuffer2D(self.buffer_size,    # data more time and num_event
                                    cols=self.num_sensors_enabled+2)
        self.data_option=RingBuffer2D(self.buffer_size,         # data = All or Muon or Electron ....
                                    cols=self.num_sensors_enabled+2,dtype=float)
        self.saved_data_buffer = RingBuffer2D(self.buffer_size,
                                    cols=self.num_sensors_enabled)
        while not self.queue.empty():
            self.queue.get()
        log.info("Buffers cleared")
        
    def reset_event_classification_live(self):
        self.Event_Muon = RingBuffer2D(self.buffer_size,cols=self.num_sensors_enabled,dtype=float)
        self.Event_muon_FitPara = RingBuffer2D(self.buffer_size,cols=1,dtype=object)
        self.All_Events_muon_FitPara = RingBuffer2D(self.buffer_size,cols=1,dtype=object)
        self.Event_HighE_Electron = RingBuffer2D(self.buffer_size,cols=self.num_sensors_enabled,dtype=float)                                             
        self.Event_Electron = RingBuffer2D(self.buffer_size,
                                    cols=self.num_sensors_enabled,dtype=float)
        self.Event_Muon_decay = RingBuffer2D(self.buffer_size,
                                    cols=self.num_sensors_enabled,dtype=float)
        self.All_Events = RingBuffer2D(self.buffer_size,
                                    cols=self.num_sensors_enabled,dtype=float)
        self.All_Events_type = RingBuffer2D(self.buffer_size,
                                    cols=1,dtype=object)
        self.Class_EventLive = {'Muon':(self.Event_Muon),'MuonFitPara':self.Event_muon_FitPara,'Electron':(self.Event_Electron),
                                    'Disintegration':(self.Event_Muon_decay),'AllEvents':(self.All_Events),
                                    'HighEnergyElectron':(self.Event_HighE_Electron),'AllEventsType':(self.All_Events_type),
                                    'AllEventsMuonFitPara':(self.All_Events_muon_FitPara)}
        log.info("Buffers live cleared size {}".format(self.buffer_size)) 
    
    def reset_event_classification_saved(self,length):
        self.Event_Muon_s = RingBuffer2D(length,cols=self.num_sensors_enabled,dtype=float)
        self.Event_muon_FitPara_s = RingBuffer2D(length,cols=1,dtype=object)
        self.All_Events_muon_FitPara_s = RingBuffer2D(length,cols=1,dtype=object)
        self.Event_HighE_Electron_s = RingBuffer2D(length,cols=self.num_sensors_enabled,dtype=float)                                             
        self.Event_Electron_s = RingBuffer2D(length,
                                    cols=self.num_sensors_enabled,dtype=float)
        self.Event_Muon_decay_s = RingBuffer2D(length,
                                    cols=self.num_sensors_enabled,dtype=float)
        self.All_Events_s = RingBuffer2D(length,
                                    cols=self.num_sensors_enabled,dtype=float)
        self.All_Events_type_s = RingBuffer2D(length,
                                    cols=1,dtype=object)
        self.Class_EventSaved = {'Muon':(self.Event_Muon_s),'MuonFitPara':self.Event_muon_FitPara_s,'Electron':(self.Event_Electron_s),
                                    'Disintegration':(self.Event_Muon_decay_s),'AllEvents':(self.All_Events_s),
                                    'HighEnergyElectron':(self.Event_HighE_Electron_s),'AllEventsType':(self.All_Events_type_s),
                                    'AllEventsMuonFitPara':(self.All_Events_muon_FitPara_s)}
        log.info("Buffers saved cleared size {}".format(length)) 
        self.Event_id_Saved=RingBuffer2D(length,
                                    cols=1,dtype=int)
################################

    def reset_event(self,key='AllEvents'):
        self.Class_EventLive[key]=RingBuffer2D(self.buffer_size,cols=self.num_sensors_enabled,dtype=float) 
        
        
    #LOAD PEDESTAL AND GAIN FILES 
    def loadCSVfile(self, file_path, key):
        if not (key == 'pedestals' or key == 'gains'):
            log.warning("Failed to load csv file: key {} not existing!".format(key))
            return
        # load from csv file
        data = np.genfromtxt(file_path)
        all_calib = np.empty(self.num_sensors)
        # Format is: uplink, channel, data (ex pedestal, gain)
        for i, line in enumerate(data):
            # checks that the channels in the csv file are correctly ordered
            if int((line[0] % 10) * self.num_channels_per_uplinks + line[1]) != i:
                log.warning("Loading {} file: Channels must be in the right order!".format(key))
            else:
                all_calib[i] = line[2]
        self.calibration_all_channels[key] = list(itertools.compress(all_calib, self.channels_enabled))
        
    #LOAD SETUP FILE
    def load_general_setup_file(self, file_path):
        # load general setup file (txt)
        # which contains the uplinks enabled and where the csv ped+gain files are
        #file_path can be loaded from the interface through MainWindow class
        #file_path is passed by the MainWindow when it starts or when we want to reload it or the pedestal and gain csv files
        log.info("Loading setup file {}".format(file_path))
         
        #lecture du fichier yalm
        with open(file_path, 'r') as f:
            cfg = yaml.load(f)
        if len(cfg['FrontEndBoardConfig']) != 8:           
            log.warning("FrontEndBoardConfig should have 8 values and not {}! Aborting setup file loading.".format(len(enabled)))
            return
            
        # enregistre les valeurs du yalm dans des variables
        self.uplinks_enabled = cfg['FrontEndBoardConfig']
        self.all_pedestal = cfg['Pedestals']['AllPed']
        self.all_pedestal_val = cfg['Pedestals']['AllPedVal']
        self.path_pedestal_file =  cfg['Pedestals']['PedFilePath']
        self.all_gain = cfg['Gains']['AllGain']
        self.all_gain_val = cfg['Gains']['AllGainVal']
        self.path_gain_file =  cfg['Gains']['GainFilePath']
        self.Threshold = cfg['Threshold']
        self.PetoMip = cfg['PetoMip']
        
        # updates channels enabled:
        self.channels_enabled = [enabled for enabled in self.uplinks_enabled for _ in range(self.num_channels_per_uplinks)]
        
        num_sensors = sum(x > 0 for x in self.uplinks_enabled) * self.num_channels_per_uplinks
        if num_sensors != self.num_sensors_enabled:
            self.num_sensors_enabled = num_sensors
            log.info("Number of sensors enabled changed to {}".format(num_sensors))
            self.reset_buffers()
            self.reset_event_classification_live()
            self.reset_event_classification_saved(self.buffer_size)
        
        # charge un array de pedestal
        if self.all_pedestal:
            if self.all_pedestal_val > 0:
                log.info("All pedestals set to {}".format(self.all_pedestal_val))
                self.calibration_all_channels['pedestals'].fill(self.all_pedestal_val)
            else:
                log.warning("Cannot set all pedestals to ", self.all_pedestal_val, "!")
        else:
            log.info("Setting pedestals from file {}".format(self.path_pedestal_file))
            self.loadCSVfile(self.path_pedestal_file, 'pedestals')
        
        # charge un array de gains
        if self.all_gain:
            if self.all_gain_val > 0:
                log.info("All gains set to {}".format(self.all_gain_val))
                self.calibration_all_channels['gains'].fill(self.all_gain_val)
            else:
                log.warning("Cannot set all gains to ", self.all_gain_val, "!")
        else:
            log.info("Setting gains from file {}".format(self.path_gain_file))
            self.loadCSVfile(self.path_gain_file, 'gains')
        
        for i,g in enumerate(self.calibration_all_channels['gains']):
            if(g==0):    
                self.calibration_all_channels['gains'][i] = 1
                log.warning("Gain {} is zero. Set it to 1.".format(i))
        
        # defines max_intensity for signal normalization
        # normalization = (MAX_adc - pedestal)/(gain * PEtoMIP)
        # with MAX_adc=4095
        
        norm_calib = np.empty(self.num_sensors_enabled)
        for i in range(self.num_sensors_enabled):
            norm_calib[i] = (self.MAX_adc - self.calibration_all_channels['pedestals'][i])/(self.calibration_all_channels['gains'][i]*self.PetoMip)
        
        self.calibration_all_channels['normalization'] = norm_calib
        log.info("Normalization factors defined for each channels enabled")
    
    #LOAD SETUP FILE
    def load_bias_voltage(self, file_path):
        # load bias voltage from general setup file (txt)
        log.info("Loading bias voltage from setup file {}".format(file_path))
         
        #lecture du fichier yalm
        with open(file_path, 'r') as f:
            cfg = yaml.load(f)
        return cfg['BiasX']
