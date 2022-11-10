def largest_difference(numberList):
    # made up a container
    differenceList = []; counter = -1
    theDifferenceOfNumber = 0
    
    
    # just for our notes - not effective
    for element in numberList:
        # try to check the difference with index before
        if(counter != -1): theDifferenceOfNumber = element - numberList[counter]
        
        # check is it a negative value or not
        if(theDifferenceOfNumber < 0): theDifferenceOfNumber *= -1
        
        # now insert our value
        differenceList.append(theDifferenceOfNumber)
        
        # and then, made up the count and reset the difference
        counter += 1; theDifferenceOfNumber = 0
      
        
    # for-loop difference check
    for number in numberList:
        
        for compareNumber in numberList:
            # check the difference
            theDifferenceOfNumber = number - compareNumber
            
            # avoid negative bugs
            if(theDifferenceOfNumber < 0): theDifferenceOfNumber *= -1
            
            # insert our number into a list
            differenceList.append(theDifferenceOfNumber)
            
            # reset theDifferenceOfNumber
            theDifferenceOfNumber = 0
            
    
    # for-loop highest score check
    highest = max(differenceList)
    
    return highest
