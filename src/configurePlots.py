import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
# file with different functions to configure plots

#-----------------------------------------------------------------------
# configuration of point size
def linear_point_size( intensity, **options ) :
    
    # scales linearly the size of points in the plot with respect to intensity
    
    maxi = 1            # maximum size of the points in local coordinates of the plot
    mini = 0            # minimum size of the points in local coordinates of the plot
    saturate_at = 1     # saturates the circle size at a certain value
    if "maxi" in options : maxi = float(options["maxi"])
    if "mini" in options : mini = float(options["mini"])
    if "saturate_at" in options : saturate_at = float(options["saturate_at"])
    if maxi<mini: maxi=mini+1
    
    scaled_size = np.where(intensity>0, (((maxi-mini)/saturate_at)*intensity + mini), intensity)
    return np.where(scaled_size>=maxi, maxi, scaled_size)

def linear_point_size3D( intensity, **options ) :
    
    # scales linearly the size of points in the plot with respect to intensity
    
    maxi = 1            # maximum size of the points in local coordinates of the plot
    mini = 0            # minimum size of the points in local coordinates of the plot
    saturate_at = 1     # saturates the circle size at a certain value
    if "maxi" in options : maxi = float(options["maxi"])
    if "mini" in options : mini = float(options["mini"])
    if "saturate_at" in options : saturate_at = float(options["saturate_at"])
    if maxi<mini: maxi=mini+1
    
    scaled_size = np.where(intensity>0, (((maxi-mini)/saturate_at)*intensity + mini), intensity)
    #return np.trim_zeros(np.where(scaled_size>=maxi, maxi, scaled_size))
    return np.where(scaled_size>=maxi, maxi, scaled_size)

pt_size = { "linear" : linear_point_size, "linear3D" : linear_point_size3D }

#-----------------------------------------------------------------------
# configuration of point color
def linear_point_colour( intensity, **options ) :
    
    # scales linearly the size of points in the plot with respect to intensity
    # see page: http://pyqt.sourceforge.net/Docs/PyQt4/qcolor.html
    # for colour definition
    
    maxi = 1    # maximum hue of the points in local coordinates of the plot
    mini = 0    # minimum hue of the points in local coordinates of the plot
    if "maxi" in options : maxi = float(options["maxi"])
    if "mini" in options : mini = float(options["mini"])
    
    colours=[]
    for j,ii in enumerate(intensity):
        col = QtGui.QColor()
        col.setHsv(((maxi-mini)*ii + mini),255,255);
        colours.append(col)
        #print(ii, ((maxi-mini)*ii + mini), col)
    
    return colours

def linear_point_colour3D( intensity, **options ) :
    
    # scales linearly the size of points in the plot with respect to intensity
    # see page: http://pyqt.sourceforge.net/Docs/PyQt4/qcolor.html
    # for colour definition
    
    maxi = 1    # maximum hue of the points in local coordinates of the plot
    mini = 0    # minimum hue of the points in local coordinates of the plot
    if "maxi" in options : maxi = float(options["maxi"])
    if "mini" in options : mini = float(options["mini"])
    
    colours=[]
    for j,ii in enumerate(intensity):
        #if ii!=0:
        col = QtGui.QColor()
        col.setHsv(((maxi-mini)*ii + mini),255,255);
        colours.append([col.red(), col.green(), col.blue(), col.alpha()])   # doesn't work nicely yet...
        #print(ii,[col.red(), col.green(), col.blue(), col.alpha()])
    
    return colours

pt_colour = { "linear" : linear_point_colour, "linear3D" : linear_point_colour3D }
