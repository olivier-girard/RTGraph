#!/usr/bin/python3
import multiprocessing
import sys
import time
import platform
import itertools
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np


import logging as log
import logging.handlers
import argparse


from gui import *
from Command import *
from DisplayMode import *

from acqprocessing import AcqProcessing
from ringbuffer2d import RingBuffer2D

class MainWindow(QtGui.QMainWindow):
    def __init__(self, acq_proc):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Know about an instance of acquisition/processing code
        # to forward GUI events
        self.acq_proc = acq_proc

        self.plt1 = None
        self.gl=None
        self.timer_plot_update = None
        self.timer_freq_update = None
        self.sp = None

        # configures
        self.configure_plot()
        self.configure_timers()
        self.configure_signals()
        
        self.sig_load_sensor_pos() # Prepare acquisition
        self.sig_load_setup_file() # initialize pedestals and gains

    def configure_plot(self):
        print("rerererere")
        self.ui.plt.setBackground(background=None)
        self.ui.plt.setAntialiasing(True)
        self.plt1 = self.ui.plt.addPlot(title ="Histogramme")
        self.img = pg.ImageItem()
        self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.img)
        self.plt1.addItem(self.img)
        self.ui.plt.addItem(self.hist)
        self.plt2 = self.ui.plt.addPlot(title ="Trace de la particule")
        # pxMode: the spots size is independent of the zoom level
        # pen: contour
        self.scatt = pg.ScatterPlotItem(pxMode=False,pen=pg.mkPen(None))
        #self.plt2.setDownsampling(ds=True, auto=True, mode='peak')
        #self.plt2.setClipToView(True)
        
        self.plt2.addItem(self.scatt)
        
        self.gl = pg.GradientLegend((10,100),(590,5)) 
        self.gl.setIntColorScale(0,10)
        self.gl.scale(1,-1)
        self.plt2.addItem(self.gl)
        
    def configure_timers(self):
        self.timer_plot_update = QtCore.QTimer(self)
        self.timer_plot_update.timeout.connect(self.update_plot)

    def configure_signals(self):
        self.ui.pButton_Start.clicked.connect(self.start)
        self.ui.pButton_Stop.clicked.connect(self.stop)
        self.ui.numIntSpinBox.valueChanged.connect(self.acq_proc.reset_buffers)
        self.ui.intCheckBox.stateChanged.connect(self.sig_int_changed)
        self.ui.sensorLoadbtn.clicked.connect(self.sig_load_sensor_pos)
        self.ui.setupLoadbtn.clicked.connect(self.sig_load_setup_file)
    
    def sig_load_sensor_pos(self):
        file_path = self.ui.sensorConfFile.text()
        print("Loading sensor description file {}".format(file_path))
        data = np.genfromtxt(file_path, dtype=np.float)
        # Format is: x,y,sensor_num
        #print(data)
        self.acq_proc.set_sensor_pos(data[:,2], data[:,3], data[:,0], data[:,1])
    
    def sig_int_changed(self):
        is_int = self.ui.intCheckBox.isChecked()
        self.acq_proc.set_integration_mode(is_int)
    
    def sig_load_setup_file(self):
        file_path = self.ui.setupGeneralFile.text()
        self.acq_proc.load_general_setup_file(file_path)

    def update_plot(self):
        tt = time.time()
        got_values = self.acq_proc.fetch_data()
        if not got_values: return
        self.data = self.acq_proc.plot_signals_map()
        #print(self.data.ravel())
        intensity, colors, maxintensity = self.acq_proc.plot_signals_scatter()
        self.img.setImage(self.data.astype(np.float))#affiche histogramme
        if(maxintensity!=0):
            self.scatt.setData(x=self.acq_proc.x_coords,
                                y=self.acq_proc.y_coords,size=((intensity/maxintensity)*10),brush=colors)#traceScatterplot
        
        #self.gl.setIntColorScale(self.acq_proc.Threshold*10,int(max(self.data)))
        nt = time.time()
        log.info("Framerate: {} fps".format(1 / (nt - tt)))
        self.classify_trace()
        #self.plt2.clear()
        
        
    def classify_trace(self):
        Mip_per_Stage=0
        Signal_per_Stage=0
        counter=[]
        Nbr_Signal_per_Stage=[] 
        Nbr_Mip_per_Stage=[]           
        for j, i in enumerate(self.acq_proc.y_coords):
            if(i!=self.acq_proc.y_coords[0]):
                self.Sensor_per_Stage=j
                break
        for j, i in enumerate(self.data[0:len(self.acq_proc.y_coords)]):
            if(i>0):
                Signal_per_Stage+=1 ## signal counter
                Mip_per_Stage+=int(round(i[0]))
            if((j+1)%self.Sensor_per_Stage==0):                
                Nbr_Signal_per_Stage.append(Signal_per_Stage)
                Nbr_Mip_per_Stage.append(Mip_per_Stage)
                Signal_per_Stage=0
                Mip_per_Stage=0
        #self.print_data(self.data)
        #print(Nbr_Signal_per_Stage, Nbr_Mip_per_Stage)
        self.data = list(itertools.compress(self.data, self.acq_proc.channels_enabled))
        self.acq_proc.All_Events.append(self.data)
        for j, i in enumerate(Nbr_Signal_per_Stage):
            if(i==1 and Nbr_Mip_per_Stage[j]<35/self.acq_proc.PetoMip):
                counter.append(1)
                if(sum(counter)==3 and j==2):
                    for j,i in enumerate(Nbr_Signal_per_Stage[3:]):
                        if(i==1 and Nbr_Mip_per_Stage[j]<35/self.acq_proc.PetoMip):   ####  TRACE
                            counter.append(1)
                            if(sum(counter)>=len(Nbr_Signal_per_Stage)-2 and j==len(Nbr_Signal_per_Stage)-4):
                                self.data = list(itertools.compress(self.data, self.acq_proc.channels_enabled))
                                self.acq_proc.Event_Trace.append(self.data)
                                self.fit_trace(plot=True)
                        if(i==0):counter.append(0)
                        if(i>1 and Nbr_Mip_per_Stage[j]>70/self.acq_proc.PetoMip):    ####  DOUCHE EECTRONIQUE
                            self.data = list(itertools.compress(self.data, self.acq_proc.channels_enabled))
                            self.acq_proc.Event_Douche.append(self.data)
                        if():
                            print()
                        
            else:counter.append(0)
        self.acq_proc.Class_Trace['Trace'].len(self.acq_proc.Class_Trace['Trace'])
        self.acq_proc.Class_Trace['Douche'].len(self.acq_proc.Class_Trace['Douche'])

    
    def print_data(self,data):
        for i,value in enumerate(data.ravel()):
            print(round(value,3),' ', end='')
            if((i+1)%self.Sensor_per_Stage==0):
                print("\n")
        print("\n")
        
        
    def fit_trace(self,plot=True):
        data=self.acq_proc.plot_signals_map().ravel()    
        x=[];y=[]
        reg_y=[0]*len(self.acq_proc.y_coords)      #y=ax+b
        a=0;b=0
        for j, i in enumerate(data):
            if(i!=0):
                for i_y in range(len(self.acq_proc.y_coords)):
                    if(i_y==j):
                        y.append(self.acq_proc.y_coords[i_y])
                for i_x in range(len(self.acq_proc.x_coords)):
                    if(i_x==j):
                        x.append(self.acq_proc.x_coords[i_x])
        if(x[0]-x[len(x)-1]!=0):
            a=(y[0]-y[len(y)-1])/(x[0]-x[len(x)-1])
            b=y[0]-a*x[0]
            reg_y=a*self.acq_proc.x_coords + b

        if plot:
            self.plt2.plot((x[0],x[len(x)-1]),(y[0],y[len(y)-1]))
            #self.plt2.plot(self.acq_proc.x_coords,reg_y)
        return reg_y
        
    
    def start(self):
        log.info("Clicked start (pipe)")
        cmd = self.ui.cmdLineEdit.text()
        self.acq_proc.start_acquisition(cmd)
        self.timer_plot_update.start(10)

    def stop(self):
        log.info("Clicked stop")
        self.timer_plot_update.stop()
        self.acq_proc.stop_acquisition()
        
    def closeEvent(self, event):
        print('Window closed: ')
        print('event: {0}'.format(event))
        if self.acq_proc.sp is not None:
            if self.acq_proc.sp.proc:
                self.acq_proc.sp.proc.terminate()
        # et ici tout ce qu'il faut potentiellement faire pour quitter comme il faut.
        event.accept()
        
class CommandWindow(QtGui.QMainWindow):
    def __init__(self,acq):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_CommandWindow()
        self.ui.setupUi(self)
        self.ui2 = Ui_MainWindow()
        self.acq=acq
        self.main=MainWindow(acq)
        self.configure_signal()
        self.main.configure_plot()
        self.main.configure_timers()
        self.main.configure_signals()
        
        
    def configure_signal(self):
        self.ui.pushButton_SavedData.clicked.connect(self.saved_data)
        self.ui.pushButton_LIVE.clicked.connect(self.live)
        #self.ui.pushButton_Right.clicked.connect()
        #self.ui.pushButton_Left.clicked.connect()
        #self.ui.pushButton_Start.clicked.connect()
        #self.ui.pushButton_Pause.clicked.connect()
        #self.ui.sensorLoadbtn.clicked.connect()
        #self.ui.setupLoadbtn.clicked.connect()
    
    def live(self):
        #slef.acq.sp=None
        log.info("Clicked start (pipe)")
        cmd="./fake_track_pebs.py"
        #"/home/lphe/usbBoard/Builds/tracker_demo_daq.sh"
        self.acq.start_acquisition(cmd)
        self.main.plt2.plot([1,2,3,1],[1,4,5,6])
        #self.plt=self.ui2.plt.addPlot().plot([1,2,3,1],[1,4,5,6])
        self.main.timer_plot_update.start(10)
        
    def pause(self):
        log.info("Clicked stop")
        self.main.timer_plot_update.stop()
    
    def data_load(self,path,cmdplay):
        #data = np.genfromtxt(file_path) # prend 2s 
        freq = 1 # Hz
        event = 0
        with open('/home/lphe/scifi-data/vata64-data/Pebs_cp-from-tell22/signal.csv') as csvfile:
                for i,row in enumerate(csvfile):
                    rowsplit = row.split()
                    rowsplit[0] = i
                    rowsplit[1] = int(time.time())
                    for element in rowsplit:
                        print("{}\t".format(element), end="")
                    time.sleep(1/freq)
                    sys.stdout.flush()
                    event += cmdplay
        
    
    def saved_data(self):
        path = self.ui.lineEdit_DataPath.text()
        self.data_load(path,1)
        
        

    
    
    
    
        
        
        
        


class DisplayModeWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_DisplayModeWindow()
        self.ui.setupUi(self)


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
    win1 = MainWindow(ap)
    win2 = CommandWindow(ap)
    win3 = DisplayModeWindow()
    
    win1.show()
    win2.show()
    win3.show()
    app.exec()

    log.info("Finishing RTGraph\n")
    log.shutdown()
    win1.close()
    win2.close()
    win3.close()
    app.exit()
    sys.exit()
    
