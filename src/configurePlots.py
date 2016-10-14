import numpy as np
import pyqtgraph as pg
# file with different functions to configure plots

#-----------------------------------------------------------------------
# configuration of point size
def linear_point_size( intensity, **options ) :
    
    # scales linearly the size of points in the plot with respect to intensity
    
    maxi = 1    # maximum size of the points in local coordinates of the plot
    mini = 0    # minimum size of the points in local coordinates of the plot
    if "maxi" in options : maxi = float(options["maxi"])
    if "mini" in options : mini = float(options["mini"])
    if maxi<mini: maxi=mini+1
    
    return np.where(intensity>0, ((maxi-mini)*intensity + mini), intensity)

pt_size = { "linear" : linear_point_size }

#-----------------------------------------------------------------------
# configuration of point color
def linear_point_colour( intensity, **options ) :
    
    # scales linearly the size of points in the plot with respect to intensity
    
    maxi = 1    # maximum hue of the points in local coordinates of the plot
    mini = 0    # minimum hue of the points in local coordinates of the plot
    if "maxi" in options : maxi = float(options["maxi"])
    if "mini" in options : mini = float(options["mini"])
    
    colours=[]
    for j,ii in enumerate(intensity):
        colours.append(pg.intColor(0, hues=((maxi-mini)*ii + mini), values=1, maxValue=255, minValue=150, maxHue=360, minHue=0, sat=255, alpha=255))
        print(ii, ((maxi-mini)*ii + mini))
    
    return colours  # does not work yet!!!

pt_colour = { "linear" : linear_point_colour }
