import string

def capital_indexes(myString):
    # make a container
    indexCount = 0
    resultList = []
    
    # analyze our string
    for char in myString:
        # if the character is a uppercase alpha, then get the index
        if (char in string.ascii_uppercase): resultList.append(indexCount)
        indexCount += 1
        
    # return our result
    return resultList
