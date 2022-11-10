def is_anagram(firstWord, secondWord):
    # made up our container
    firstList = []; secondList = []
    
    # convert firstWord into firsList
    for char in firstWord: firstList.append(char)
        
    # convert secondWord into secondList
    for char in secondWord: secondList.append(char)
    
    # sort it's list before compare
    firstList.sort(); secondList.sort()
    
    # now compare it, return True if it's the same
    if(firstList == secondList): return True
    else: return False
