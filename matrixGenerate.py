

# To create more light-weightened matrix with uint8
import numpy as np

# To find width and height of the terminal
import shutil

from time import sleep


import string

# To clear console
from os import system

# For adding extra symbols beside the white space
import random

# For calculating the chance of spawning for zeros;
# exp()
# sqrt()
# .trunc()
import math

# Returns current WIDTH of terminal;
def width():
    width = shutil.get_terminal_size()[0]
    # print('width is ', width)
    return width

# Returns current HEIGHT of terminal;
def height():
    height = shutil.get_terminal_size()[1]
    # print('Height is ', height)
    return height

# Initializes and prints EMPTY(means with white spaces ords only) matrix for the first run;
# Actually it has first full-zero line;
def createEmptyMatrix(height, width): 
    emptyMatrix = []

    
    # Fills the matrix with white spaces;
    for i in range(0, height()):

        # Adding new line
        emptyMatrix.append([])
        for j in range (0, width()):
            emptyMatrix[i].append(ord(' '))



    # Clears memory (do I really need this thing?);
    del(i, j)

    # printFilledMatrix(emptyMatrix) 
    return(emptyMatrix)  

# Prints an updated(with added symbols) matrix;
def printFilledMatrix(filledMatrix):

    for i in range(np.shape(filledMatrix)[0]):

        # Creates a template to be filled and printed later;
        currentLine = ''
        for j in range(np.shape(filledMatrix)[1]):

            # Adds to a line corresponding char from matrix;
            currentLine += chr(filledMatrix[i][j])

        # An auxiliary shit to check whether the terminal is filled;
        currentLine = currentLine[:-1]
        currentLine += '|'
        print(currentLine)
    

# Returns multiplicator for normal distribution of zeros in line;
def normalDistribution(width, indexOfElement):
    sigma = math.trunc(width/5)
    mu = sigma*2.5
    fract = (1)/(sigma*math.sqrt(2*3.14))
    power = math.exp(-0.5*((indexOfElement-mu)/sigma)*((indexOfElement-mu)/sigma))
    chanceMultiplicator = (fract*power)
    return chanceMultiplicator


def charOrWhiteSpace(elementOfMatrix):
    if (random.randint(0, width()) <= math.trunc(normalDistribution(width(), x)*8000)):
        elementOfMatrix += chr('0')
    else:
        elementOfMatrix += chr(' ')  
        return elementOfMatrix  


def fillFirstTwoLines(emptyMatrix):

    # Fills the first line with zeros; 
    for j in range(0, np.shape(emptyMatrix)[1]):
        emptyMatrix[0][j] = ord('0')
        emptyMatrix[1][j] = charOrWhiteSpace()

    




# Clears the terminal
def clear():
    _ = system('clear')




# def fillMatrix(emptyMatrix):

#     for i in range(np.shape(emptyMatrix)[0]):
#         for j in range(np.shape(emptyMatrix)[1]):
#             if (random.randint == )


#     printFilledMatrix(emptyMatrix)
while 1:
    for _ in range(height()):
        testLine = ''
        for x in np.arange(0, width(), 1):
            # print(normalDistribution(100, x))
            if (random.randint(0, width()) <= math.trunc(normalDistribution(width(), x)*8000)):
                testLine += '0'
            else:
                testLine += ' '

        print(testLine)    
    sleep(0.005)
# in lieu -- взамен



# Main
# while 1:

#     createEmptyMatrix(getHeightOfTerminal(), getWidthOfTerminal()) #26*116
#     print(chr(332))
#     sleep(5)
#     clear()
    
 

# ' ' --- 32
# 0   --- 48 
# o   --- 111
# O   --- 79
# Ō   --- 332
# ȱ   --- 561
# ọ   --- 7885
# Ộ   --- 7896
# ộ   --- 7897
# ʘ   --- 664
# ˚   --- 730
# ˟   --- 735
# ˣ   --- 739
# Θ   --- 920
# θ   --- 952 
# Ϙ   --- 984
# Ͼ   --- 1022
# Ͽ   --- 1023
# ѳ   --- 1139
# Ѻ   --- 1146
# ѻ   --- 1147
# ୦   --- 2918
# ○   --- 9675
