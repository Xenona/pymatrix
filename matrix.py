import random
import time;

# TO DO:
# Move constants into external file
# Move Main() into external file
# Revers it so treads will actually fall, not rise
# Create matrix and replace symbols?
# Array of additional symbols needed to fill white spaces

screenWidth = 50;
timeBetweenPrints = 0.5;

def printWithDelay(lineToBePrinted):
    # Actually a procedure that just prints given line with delay;
    # Delay value is set with timeBetweenPrints;
    time.sleep(timeBetweenPrints)
    print(lineToBePrinted)



def createInitiateLine (screenWidth):
    # Returns one first line with probability of 1/10 for zero and 9/10 to white space;
    # Width of line is set with screenWidth;
    # Also prints the made-up line;

    initiateLine = ''
    for _ in range (1, screenWidth+1):
        if (random.randint(0,10) == 1):
            initiateLine += '0'
        else:
            initiateLine += ' '
  
    return initiateLine   


def printLines(previousLine):


    print('INI LINE:' + previousLine)
    
    currentLine = ''
    for i in range(0, screenWidth):
        if (previousLine[i] == '0'):
            print('If0 init' + currentLine)
            # Choose whether to continue thread if was zero;
            if (random.randint(0,10) != 1):
                currentLine += '0'
            
            else:
                currentLine += ' '
            print('aft rand' + currentLine)
        else:

            # Choose whether to put extra symbol instead of white space
            # With opportunity to start a thread 
            if (random.randint(0,20) == 0):
                currentLine += "\033[94m" + '.' + "\033[0m"
            elif (random.randint(0,101) == 1):
                currentLine += '0'
            else:
                currentLine += ' '


   
    previousLine = currentLine
    # print('RES LINE IN FUNCTION:' + previousLine)
 
    currentLine = ''
    return(previousLine)


previousLine = createInitiateLine(screenWidth)
print(previousLine)
i = 1
while input():

    # printWithDelay(previousLine)
    previousLine = printLines(previousLine)

    i += 1
    
   
    # создаём ещё одну переменную, которая хранит длину каждой цепочки нулей 