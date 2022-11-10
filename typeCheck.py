def only_ints(charOne, charTwo):
    # avoid for (1, True) and the other identic bugs
    if(isinstance(charOne, bool) or isinstance(charTwo, bool)): return False

    # check are they an integer, if double True then True
    if(isinstance(charOne, int) and isinstance(charTwo, int)): return True
    
    # otherwise, return False
    else: return False
