# let's build our easy peasy function!
def list_xor(n, list1, list2):
    # check is it just the same or no
    if(n in list1 and n in list2): return False
    
    # when the bool output is the same, it's a False
    elif(n not in list1 and n not in list2): return False
    
    # okay now return our value
    return True
