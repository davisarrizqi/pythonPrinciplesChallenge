# [ PYTHON PRINCIPLES CHALLENGE ] - SOLUTION

This is a solution for Python Principles Challenge,
you can use this script if you're stuck when you
try to finish the Python Principles Challenge

This repository is created by Davis



# CODE SAMPLE - THOUSAND SEPARATOR

Maybe this script can be useful when you
want to get the better value for display
some value like for innerHTML with flask

<code>
import math

def format_number(myNumber):
    if(myNumber < 0):
        return None
        
    else:
        # make a container
        listNumber = []; stringResult = ''
        
        # convert our number --> string --> list
        for num in str(myNumber):
            listNumber.append(num)
            
        # add some helper tools
        countHelper = -3; numberLength = len(listNumber)
        repeatHowManyTimes = round(numberLength/3)
        
        # make sure it's digit more than 4
        if(numberLength >= 4):
            for addCommas in range(repeatHowManyTimes):
                listNumber.insert(countHelper, ',')
                countHelper -= 4
        
        # avoid comma's bug        
        if(listNumber[0] == ','):
            del listNumber[0]
            
        # convert our list into a string
        for num in listNumber:
            stringResult += num
            
        # FINISH HIM !!!
        return(stringResult)
        
# Debug for our Result
print(format_number(10000000000000000))

</code>
    
# ENJOY!
