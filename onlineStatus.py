# declare our statuses
statuses = {
    'Alice' : 'online',
    'Bob' : 'offline',
    'Eve' : 'online'
}

def online_count(myDict):
    # make a container
    counter = 0
    
    # start counting with for loop
    for element in myDict:
        if(myDict[element] == 'online'): counter += 1  # count
        
    return counter
