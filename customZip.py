def zap(a, b):
    # let's make a container
    finalResult = []
    
    # declare for the length
    length = len(a)
    if(len(b) < len(a)): length = len(b)
    
    # element inserting
    for count in range(length):
        finalResult.append((a[count], b[count]))
        
    # return the value
    return finalResult


print(zap([0, 1, 2, 3], [5, 6, 7, 8]))
