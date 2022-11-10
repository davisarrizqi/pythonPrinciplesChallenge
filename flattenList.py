def flatten(myList):
    # made up our container
    resultList = []
    
    # start our logic
    for firstRange in range(len(myList)):
        for secondRange in range(len(myList[firstRange])):
            resultList.append(myList[firstRange][secondRange])
            
    # now return our value
    return resultList
