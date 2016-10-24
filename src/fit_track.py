import numpy as np
import math
import matplotlib.pyplot as plt

## Lest_squares is the one that works.
## Iterative least_squares repeates the least_squares weighting the points by the inverse of the residual
## meaning that points far away become less and less important. Fit stops when the parameters
## changes less than 0.1% from the previous iteration. (Works great!)

# reject hits based on a simple pattern recognition proposed by Fred (top layer and calculation of angle for each hit)
def reject_hits_pattern_recognition(x_array,y_array, x_para,y_para,dist_thrs):
    #print("xmin=",x_para["min"],"   xmax=",x_para["max"],"   xpitch=",x_para["pitch"])
    #print("ymin=",y_para["min"],"   ymax=",y_para["max"],"   ypitch=",y_para["pitch"])
    
    all_x = np.arange(x_para["min"],x_para["max"]+x_para["pitch"],x_para["pitch"])
    all_pts_top = [ (xi,y_para["max"]) for xi in all_x ]
    all_y = np.arange(y_para["min"],y_para["max"]+y_para["pitch"],y_para["pitch"])
    
    smallest_angle_diff = abs(math.atan((y_para["max"]-y_para["min"])/(x_para["max"]-x_para["min"])) - math.atan((y_para["max"]-y_para["min"])/(x_para["max"]-x_para["pitch"]-x_para["min"])))
    angle_bin_size = smallest_angle_diff
    
    allpts = list(zip(x_array, y_array))
    angle_toppos = []
    #print("all_pts_top=",all_pts_top)
    print("allpts=",allpts)
    vertical_line_missing = []
    for i,(xi,yi) in enumerate(allpts):
        if yi != y_para["max"]:
            for (xti,yti) in all_pts_top:
                if xti != xi:
                    slope = (yi-yti)/(xi-xti)
                    angle = math.atan(slope) - 0.5*math.pi
                    angle_toppos += [(angle,xti)]
                else:
                    angle_toppos += [(0,xti)]
        else:
            # fill with vertical line in angle vs x_top
            vertical_line_missing.append(xi)
    
    # builds the histogram (for angles)
    xbinsize = x_para["pitch"]
    nbinx = int(1 + (all_x[-1]-all_x[0])/xbinsize)
    nbiny = int(1 + math.pi/angle_bin_size)
    H1, xedges, yedges = np.histogram2d([ y for (x,y) in angle_toppos ], [ x for (x,y) in angle_toppos ], range=[[x_para["min"]-0.5*x_para["pitch"],x_para["max"]+0.5*x_para["pitch"]],[-0.5*math.pi-0.5*angle_bin_size,0.5*math.pi+0.5*angle_bin_size]], bins=[nbinx,nbiny])
    xcenters = 0.5*(xedges[1:]+xedges[:-1])
    ycenters = 0.5*(yedges[1:]+yedges[:-1])
    for vertical in vertical_line_missing:
        for ycen in ycenters:
            angle_toppos += [(ycen,vertical)]
    H, xedges, yedges = np.histogram2d([ y for (x,y) in angle_toppos ], [ x for (x,y) in angle_toppos ], range=[[x_para["min"]-0.5*x_para["pitch"],x_para["max"]+0.5*x_para["pitch"]],[-0.5*math.pi-0.5*angle_bin_size,0.5*math.pi+0.5*angle_bin_size]], bins=[nbinx,nbiny])
    #print("xedges=",xedges)
    #print("yedges=",yedges)
    print("xcenters=",xcenters)
    #print("ycenters=",ycenters)
    #print("H=",H)
    #idx = list(H.flatten()).index(H.max())
    #print("idx=",idx)
    # Finds where the maximum is (finds only one maximum)
    max_pos = np.unravel_index(H.argmax(), H.shape)
    print("max_pos=",max_pos,"   Hmax=",H.max())
    angle_at_max = ycenters[max_pos[1]]
    xtop_at_max = xcenters[max_pos[0]]
    print("angle_at_max=",angle_at_max,"   xtop_at_max=",xtop_at_max)
    print("angle_bin_size=",angle_bin_size)
    
    xt_each_layer = [ xtop_at_max + (y_para["max"] - yti)*math.tan(angle_at_max) for yti in all_y ]
    print("xt_each_layer=",xt_each_layer)
    
    """extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
    plt.imshow(H, extent=extent, interpolation='nearest')
    plt.colorbar()
    plt.show()
    input("Waiting for you to click!\n")"""
    

# recognition of pattern from calculating slope and offset of each comibination of two hits
def reject_hits_pattern_recognition2(x_array,y_array,x_para,y_para,dist_thrs):
    
    """all_x = np.arange(x_para["min"],x_para["max"]+x_para["pitch"],x_para["pitch"])
    all_pts_top = [ (xi,y_para["max"]) for xi in all_x ]"""
    all_y = np.arange(y_para["min"],y_para["max"]+y_para["pitch"],y_para["pitch"])
    
    max_inv_slope = (x_para["max"]-x_para["min"])/y_para["pitch"]
    min_inv_slope = -1*max_inv_slope
    slope_bin_size = x_para["pitch"]/y_para["pitch"]
    slope_nbins = int(1 + (max_inv_slope-min_inv_slope)/slope_bin_size)
    
    max_offset = 2*x_para["max"] - x_para["min"]    # first guess
    min_offset = 2*x_para["min"] - x_para["max"]
    offset_bin_size = x_para["pitch"]
    offset_nbins = int(1 + (max_offset-min_offset)/offset_bin_size)
    
    allpts = list(zip(x_array, y_array))
    slope_vs_offset = []    # we take the inverse of the slope to avoid infinite slope
    print("allpts=",allpts)
    points_already_analyzed = []
    for i,(x1,y1) in enumerate(allpts):
        for j,(x2,y2) in enumerate(allpts):
            if y2 != y1 and (x2,y2) not in points_already_analyzed:
                inverse_slope = (x1-x2)/(y1-y2)
                offset = x1 - inverse_slope*y1
                slope_vs_offset += [(inverse_slope,offset)]
    
    #print("slope_vs_offset=",slope_vs_offset)
    # builds the histogram
    Hrange=[[min_inv_slope-0.5*slope_bin_size,max_inv_slope+0.5*slope_bin_size],[min_offset-0.5*offset_bin_size,max_offset+0.5*offset_bin_size]]
    H, xedges, yedges = np.histogram2d([ x for (x,y) in slope_vs_offset ], [ y for (x,y) in slope_vs_offset ], range=Hrange, bins=[slope_nbins,offset_nbins])
    xcenters = 0.5*(xedges[1:]+xedges[:-1])
    ycenters = 0.5*(yedges[1:]+yedges[:-1])
    # Finds where the maximum is (finds only one maximum)
    max_pos = np.unravel_index(H.argmax(), H.shape)
    print("max_pos=",max_pos,"   Hmax=",H.max())
    offset_at_max = ycenters[max_pos[1]]
    inv_slope_at_max = xcenters[max_pos[0]]
    print("offset_at_max=",offset_at_max,"   inv_slope_at_max=",inv_slope_at_max)
    
    xt_each_layer = { yti: inv_slope_at_max*yti + offset_at_max for yti in all_y }
    print("xt_each_layer=",xt_each_layer)
    
    xout = []
    yout = []
    for i,(x1,y1) in enumerate(allpts):
        distance = abs(xt_each_layer[y1] - x1)
        if distance <= dist_thrs:
            xout += [x1]
            yout += [y1]
    
    print("xout=",xout)
    print("yout=",yout)
    print(len(x_array)-len(xout),"point(s) removed!")
    
    return xout,yout
    

def correlation(points) :
    # From: http://mathworld.wolfram.com/CorrelationCoefficient.html
    mean_x = sum( [ x for (x,y) in points ] )/len(points)
    x2 = sum( [ (xi - mean_x)**2 for (xi,yi) in points ] )
    mean_y = sum( [ y for (x,y) in points ] )/len(points)
    y2 = sum( [ (yi - mean_y)**2 for (xi,yi) in points ] )
    xy = sum( [ (xi - mean_x)*(yi - mean_y) for (xi,yi) in points ] )
    if x2==0 or y2==0:
        return 1
    return (xy**2)/(x2*y2)

# Reject points based on the correlation of all points
def reject_hits(x_array,y_array):
    # First we remove points far away
    #print("mean=",sum(x_array)/len(x_array))
    
    allpts = list(zip(x_array, y_array))
    for i,(xi,yi) in enumerate(allpts):
        corr_all_pts = correlation(allpts)
        remaining_pts = [ pt for pt in allpts if pt!=allpts[i] ]
        corr_remaining = correlation(remaining_pts)
        print("allpts=",allpts)
        print("pt=",allpts[i],"   corr_before=",corr_all_pts,"   corr_without_pt=",corr_remaining)
        if(corr_remaining > corr_all_pts):
            if( (corr_remaining-corr_all_pts)/corr_all_pts > 0.8 or (corr_remaining-corr_all_pts) > 0.2 ):
                print(allpts[i],"removed!")
                allpts.remove(allpts[i])
    
    # remove points on the same layer
    y_unique = list(set([ y for (x,y) in allpts ]))
    y_unique.reverse()
    if len(y_unique) == len([ y for (x,y) in allpts ]):
        return [ x for (x,y) in allpts ], [ y for (x,y) in allpts ]
        
    for floor in y_unique:
        pts = [ (xi,yi) for (xi,yi) in allpts if yi == floor ]  # pts on the same floor
        remaining_pts = [ (xi,yi) for (xi,yi) in allpts if yi != floor ]  # pts on the other floors
        if len(pts) > 1:    # if more than one point at this layer
            corrs = []
            for pt in pts:  # calculates correlation with all points on the same layer
                with_this_pt = remaining_pts + [pt]
                print("with_this_pt=",with_this_pt)
                corrs.append(correlation(with_this_pt))
                print("corrs=",corrs)
            
            # finds maximum correlation
            indmax = corrs.index(max(corrs))
            for i in range(len(pts)) :
                if i != indmax :
                    # remove the points which did not yield the maximum correlation
                    allpts.remove(pts[i])
                    
    return [ x for (x,y) in allpts ], [ y for (x,y) in allpts ]

def get_weights(m,y0,xv,yv,wv=None) :
    
    nws = []
    if wv is None : wv = [1.]*len(x)
    for x,y,w in zip(xv,yv,wv) :
        res = abs(y - ( m * x + y0 ))
        if res < 1e-9 : res = 1e-9
        nw = w * 1./res
        #if nw > 1e9 : nw = 1e9  # maximum weight
        if nw > 1e2 : nw = 1e2  # maximum weight
        if nw < 1e-2 : nw = 1e-2  # maximum weight
        nws.append(nw)

    return nws

def iterative_least_squares(x,y,precision=0.01) :
    
    #x,y = reject_hits(xini,yini)
    
    w = [1.]*len(x)
    prevm, prevy0 = -1e10, -1e10
    m, y0, it = 0, 0, 0
    while True :
        
        m,y0 = least_squares_w(x,y,w)
        
        print("Iteration: ", it)
        print("\nm = {0}, y0 = {1}\n".format( m, y0 ))

        if m is None : break
        if abs( (m - prevm) / m ) < precision and abs( (y0 - prevy0) / y0 ) < precision : break
        if it > 20:
            print("ATTENTION: Fit did not converge!")
            break
        prevm = m
        prevy0 = y0
        
        w = get_weights(m,y0,x,y,w)
        it+=1
    
    """
    if m is not None:
        # this is not truly the chi2, it's the perpendicular offset !!!
        chi2 = sum([ wi*(yi - (m*xi + y0))**2 for (xi,yi,wi) in zip(x,y,w)] )/(1+(m**2))
        # kind of effective error = projection of sigma_i on a perpendicular to the fit line
        error = (1./math.sqrt(12))*math.sin(math.atan(m))
        chi2 /= (error*error*(len(y)-2))
    else:
        mean_x = sum( x ) / len(x)
        chi2 = sum([ (xi - mean_x)**2 for xi in x] )
        error = (1./math.sqrt(12))
        chi2 /= (error*error*(len(y)-2))
        return None, mean_x, chi2"""
    
    error = 1./math.sqrt(12)
    if m is not None:
        chi2 = sum([ wi*(yi - (m*xi + y0))**2 for (xi,yi,wi) in zip(x,y,w)] )
    else:
        chi2 = 0 # not true !!!
    chi2 /= sum(w) 
    chi2 /= (error*error*((len(y)-2)/len(y)))
    
    return m,y0,chi2

def least_squares( x, y ) :

    if len(x) != len(y) :  
        print("ATTENTION: x and y have different lenghts, no fit performed")
        return
    
    if len(x) == 0 :
        return
        
    N = len(y)
    mean_x = sum( x ) / float(N)
    denom = sum( [ (xi - mean_x)**2 for xi in x ] )
    if denom < 1.e-6 :  #vertical line
        error = (1./math.sqrt(12))
        chi2 = denom/(error*error*(len(y)-2))
        return None, mean_x, chi2
    
    mean_y = sum( y ) / float(N)
    
    xy = []
    for xi,yi in zip(x,y) :
        xy.append((xi - mean_x)*(yi - mean_y))
    
    sum_xy = sum( xy )
    m = sum_xy / denom 
    y0 = mean_y - m*mean_x
    
    """
    # this is not truly the chi2, it's the perpendicular offset !!!
    chi2 = sum([ (yi - (m*xi + y0))**2 for (xi,yi) in zip(x,y)] )/(1+(m**2))
    # kind of effective error = projection of sigma_i on a perpendicular to the fit line
    error = (1./math.sqrt(12))*math.sin(math.atan(m))
    chi2 /= (error*error*(len(y)-2))"""
    
    error = 1./math.sqrt(12)
    chi2 = sum([ (yi - (m*xi + y0))**2 for (xi,yi) in zip(x,y)] )
    chi2 /= (error*error*(len(y)-2))
    
    return m,y0,chi2

def least_squares_w( xv, yv, w ) :

    if len(xv) != len(yv) != len(w) :  
        print("ATTENTION: x and y (and w) have different lenghts, no fit performed")
        return

    sumw = sum(w)
    x,y,x2,xy = [],[],[],[]
    for xi,yi,wi in zip(xv,yv,w) :
        x.append(wi*xi)
        y.append(wi*yi)
    
    mean_x =  sum(x) / float(sumw)
    mean_y =  sum(y) / float(sumw)

    for xi,yi,wi in zip(xv,yv,w) :
        xy.append(wi*(xi - mean_x)*(yi - mean_y))
        x2.append(wi*(xi - mean_x)**2)
    
    denom = sum(x2)
    if abs(denom) < 1.e-12 : return None, xv[0]
    
    sum_xy = sum( xy )
    m = sum_xy / denom 
    y0 = mean_y - m*mean_x
    
    return m,y0
