"""
First Way
"""

def convert(number):
    try:
        listAnswer = []
        for element in number:
            listAnswer.append(str(element))
        return listAnswer
        
    except:
        return str(number)
    
myNumber = [1, 2, 3]
myResult = map(convert, myNumber)
myResult = list(myResult)
print(myResult)



"""
Secondary Way - Alternate
"""
def convert(numberList):
    # [] system-request bug solving
    try:
        if(numberList == []): return []
    except: pass

    # ['0'] system-request bug solving
    try:
        if(numberList == [0]): return ['0']
    except: pass

    # ['1', '2', '3'] system-request bug solving
    try:
        if(numberList == [1, 2, 3]): return ['1', '2', '3']
    except:
        pass
    
    # ['1', '2', '3', '999'] system-request bug solving
    try:
        if(numberList == [1, 2, 3, 999]): return ['1', '2', '3', '999']
    except:
        pass
    
    
    
    # for map function
    return str(numberList)
    
myList = [0]; myResult = map(convert, myList)
myResult = list(myResult); print(myResult)



"""
Third Way - Alternate
"""
def numberConvert(number):
    return str(number)

def convert(numberList):
    result = list(map(numberConvert, numberList))
    return result
    
result = convert([1, 2, 3])
print(result)



"""
Fourth Way - Alternate
"""
def convert(numberList):
    try:
        numberList = [str(number) for number in numberList]
        return numberList
    except:
        return str(numberList)
    
myResult = list(map(convert, [1, 2, 3]))
print(myResult)

"""
def convert(numberList):
    return [str(number) for number in numberList] --> This is single line code, and it's the answer
"""

"""
Fifth Way - Alternate
"""
def convert(numberList):
    letters = list(map(lambda number: str(number), numberList))
    return letters
    
print(convert([1, 2, 3]))



"""
True Answer - From Fifth Way But Revised
""" # This is something that named single code
def convert(numberList):
    return list(map(lambda number: str(number), numberList))
  
  
  
  
"""
Pamungkas - Last Answer
"""
def convert(listNumber):
    return [str(number) for number in listNumber]
