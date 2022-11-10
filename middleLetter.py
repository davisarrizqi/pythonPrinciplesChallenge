def mid(myWord):
    # if its length can divided by 2, then return empty string
    if(len(myWord)%2 == 0):
        return ''
        
    # if its length can't divided by 2, then start its process
    else:
        indexPoint = (len(myWord) - 1)/2        # get the middle index
        middleValue = myWord[int(indexPoint)]   # get the middle value
      
    # FINISH HIM !!!
    return middleValue
