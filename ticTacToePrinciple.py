# our content
board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    [" ", " ", " "],
]

# first row
print(" %s | %s | %s" % (board[0][0], board[0][1], board[0][2]))

# divider row
print('-----------')

# second row
print(" %s | %s | %s" % (board[1][0], board[1][1], board[1][2]))

# divider row
print('-----------')

# third row
print(" %s | %s | %s" % (board[2][0], board[2][1], board[2][2]))


def get_row_col(code):
    # made up a container
    resultContainer = []; columnContainer = ['A', 'B', 'C']
    columnLowerContainer = ['a', 'b', 'c']
    
    # insert into our resultContainer
    for char in code:
        resultContainer.append(char)
        
    # change the alpha character into a number
    try:
        resultContainer[0] = columnContainer.index(resultContainer[0])
    except:
        try: resultContainer[0] = columnLowerContainer.index(resultContainer[0])
        except: pass
    
    # change the number so that we can use it
    resultContainer[1] = int(resultContainer[1]) - 1
    
    # made it up into a tuple, do a switch
    # switch because C1 is column-row
    # something that we need is row-column notation
    tupleResult = (resultContainer[1], resultContainer[0])
    
    # now see the result
    return tupleResult
    
print(get_row_col('A3'))
