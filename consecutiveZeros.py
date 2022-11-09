def consecutive_zeros(binaryNumber):
    # declare our container
    scoreCounter = 0; scoreList = []
    finalResultHighScorer = 0
    
    # let's make it out!
    for number in binaryNumber:
        if(number == "0"): scoreCounter += 1
        elif(number != "0"): scoreList.append(scoreCounter); scoreCounter = 0
        
        if(number == binaryNumber[-1]):
            scoreList.append(scoreCounter)
            
    # declare the highest number
    finalResultHighScorer = max(scoreList)
    return finalResultHighScorer
    
tryResult = consecutive_zeros('101')
print(tryResult)
