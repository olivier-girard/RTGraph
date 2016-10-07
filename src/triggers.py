#import numpy as np
#from ringbuffer2d import RingBuffer2D

def trigger_5layers( datagrid, options = {} ) :
    
    # Trigger if there is at least some signal in the first 5 layers 
    
    fire_trigger = True
    for l in datagrid[0:5] :
        if sum([ ch[0] for ch in l] ) < 1e-6 : 
            fire_trigger = False
    
    return fire_trigger


triggers = { "5layers" : trigger_5layers }
