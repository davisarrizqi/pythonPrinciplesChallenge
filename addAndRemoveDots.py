import string

def add_dots(myWord):
    # made up for our container
    indexPosition = 1; wordList = []
    listForCharacter = []
    
    # append all of the character
    for char in string.ascii_uppercase: listForCharacter.append(char)
    for char in string.ascii_lowercase: listForCharacter.append(char)
    
    # convert into a list
    for char in myWord: wordList.append(char)
    
    # add some dots
    for rangeDots in range(len(myWord)):
        try:
            for dotsImporting in wordList:
                if (indexPosition > 0 and wordList[indexPosition-1] in listForCharacter and wordList[indexPosition] in listForCharacter):
                    wordList.insert(indexPosition, '.')
            indexPosition += 2
            
        except:
            pass
        
    # change myWord but make sure its empty first
    myWord = ''
    
    # convert our list into a string
    for char in wordList:
        myWord += char
    
    # now return our value
    return myWord

def remove_dots(myWord):
    # made up our container
    listMyWord = []
    
    # convert myWord into a list
    for char in myWord:
        listMyWord.append(char)
        
    # delete each dots
    for element in listMyWord:
        if(element == '.'): listMyWord.remove(element)
    
    # delete again, avoid bugs
    while('.' in listMyWord):
        listMyWord.remove('.')
    # note --> if you just use this to delete the dots, it's enough
        
    # change myWord but make sure it's empty first
    myWord = ''
    
    # convert our list into a string
    for element in listMyWord:
        myWord += element
        
    # now return our result
    return myWord
    
print(remove_dots(add_dots('Devi')))
print(add_dots('Devi'))
