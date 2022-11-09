def all_equal(wantedList):
    # save it for later
    finalResult = False
    
    # index checking
    for element in wantedList:
        for subElement in wantedList:
            if (element != subElement):
                return False
                
            else:
                finalResult = True
                
    # confirm that is the same
    if(finalResult == True): return True
    
    # made up an alternate if the list is empty
    if(len(wantedList) == 0): return True
