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
