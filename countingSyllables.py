def count(myWord):
    # count the word
    totalCount = 1
    
    # analyze myWord
    for char in myWord:
        if(char == '-'): totalCount += 1    # detect by its '-'
        
    # here we are..
    return totalCount
