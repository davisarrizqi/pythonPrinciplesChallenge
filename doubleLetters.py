def double_letters(myWord):
    # let's make a container
    charBefore = ''; counter = 0
    isHaveWellDone = False
    
    # let's start our logic
    for char in myWord:
        # made it up
        if(char == charBefore): return True   # drop it like it's hot
        else: isHaveWellDone = True           # save it later
        
        # save the character
        charBefore = char
        
    # return if there is no doubleChar
    return False
