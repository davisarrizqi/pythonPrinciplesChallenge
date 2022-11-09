# *variable --> tuple type [*args]
# **variable --> dict type [**kwargs]

def param_count(*number):
    # container for how much the parameter
    counter = 0
    
    # loop count for how much the parameter
    for myNumber in number:
        counter += 1
        
    # come on!
    return counter
