

def trigger_nlayers( datagrid, **options ) :
    
    # Trigger if there is at least some signal in the first n layers 
    
    nlayers = 5
    if "layers" in options : nlayers = int(options["layers"])
    if nlayers > len(datagrid) : nlayers = len(datagrid)
    
    fire_trigger = True
    for l in datagrid[0:nlayers] :
        if sum([ ch[0] for ch in l] ) < 1e-6 : 
            fire_trigger = False
            break
    
    return fire_trigger

def trigger_n_any_layers( datagrid, **options ) :
    
    # Trigger if there is at least some signal in n layers at any position
    
    nlayers = 5
    if "layers" in options : nlayers = int(options["layers"])
    if nlayers > len(datagrid) : nlayers = len(datagrid)
    
    nsig = 0
    for l in datagrid :
        if sum([ ch[0] for ch in l] ) > 1e-6 : 
            nsig +=1
    
    if nsig >= nlayers : return True 
    return False

triggers = { "nlayers" : trigger_nlayers, "n_any_layers" : trigger_n_any_layers }
