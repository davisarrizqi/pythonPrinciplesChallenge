def palindrome(myWord):
    # made up a container
    invertedWordList = []; stringResult = ''
    
    # insert our character into our list
    for char in range(len(myWord) + 1):
        if(char == 0): continue
        else: invertedWordList.append(myWord[char * -1])
        
    # convert our list into a string
    for char in invertedWordList:
        stringResult += char
        
    # FINISH HIM!
    if(stringResult == myWord):
        return True
        
    else:
        return False
