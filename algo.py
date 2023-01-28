import numpy as np
import random
import time
import shutil
from os import system
import math

def height():
    height = shutil.get_terminal_size()[1]
    # print('height is ', height)
    return height

def width():
    width = shutil.get_terminal_size()[0]
    # print('width is ', width)
    return width

def printVector(vector, height, width):
    for i in range(height):
        lineToPrint = '' 
        for j in range(width):
            lineToPrint += vector[i][j]
        print(lineToPrint)

# Clears the terminal
def clear():
    _ = system('clear')


def main():    
    currentWidth = width()
    currentHeight = height()
    vector = np.array([[' ']*width()]*height())
        
    while 1: 

        if ((currentHeight != width()) or (currentWidth != height())):
            currentWidth = width()
            currentHeight = height()
            vector.resize(currentHeight, currentWidth)


        

        clear()
        printVector(vector, currentHeight, currentWidth)
        vector = np.roll(vector, 1, axis = 0)
        if (vector[0][1] == '0'):
            if (random.randint(0, 10) < 3): 
                vector[0][0] = ' '
            else: 
                vector[0][0] = '0'
        if (vector[1][0] == ' ' or vector[1][0] == ''):
            if (random.randint(0, 50) < 8):
                vector[0][0] = '0'
            else:
                vector[0][0] = ' '
        time.sleep(0.05)

# Returns multiplicator for normal distribution of zeros in line;
def normalDistribution(width, indexOfElement):
    sigma = math.trunc(width/5)
    mu = sigma*2.5
    fract = (1)/(sigma*math.sqrt(2*3.14))
    power = math.exp(-0.5*((indexOfElement-mu)/sigma)*((indexOfElement-mu)/sigma))
    chanceMultiplicator = (fract*power)
    return chanceMultiplicator


def prepareLine(coefficient, currentWidth):

     

    # print(previousVector)
    nextVector = [' ']*currentWidth 
    # print(coefficient)
    for x in range(0, currentWidth):

        
        # if ((previousVector[x] == '0') and (previousVector[x-1]) and (previousVector[x+1]) and random.randint(1, width()) <= math.trunc(normalDistribution(width(), x)*coefficient)):
        #     nextVector[x] = '0'
        # elif (random.randint(1, width()) <= math.trunc(normalDistribution(width(), x)*coefficient/2)):
        #     nextVector[x] = '0'
        # else:
        #     nextVector[x] = ' '

        if (random.randint(1, currentWidth) <= math.trunc(normalDistribution(width(), x)*coefficient)):
            nextVector[x] = '0'
        else:
            nextVector[x] = ' '    

    # print(matrix)
    # print(nextVector)
    return nextVector


def printMatrix(matrix, currentHeight, currentWidth):
    for i in range(currentHeight-1):
        lineToBePrinted = ''
        for j in range(currentWidth):
            if ((matrix[i][j] == '0') and (matrix[i+1][j] == ' ')):
                lineToBePrinted +=  "\033[37m" + matrix[i][j] + "\033[0m"
            else:
                lineToBePrinted += matrix[i][j]
        print(lineToBePrinted)

def printMatrixOrd(matrix, currentHeight, currentWidth):
    for i in range(currentHeight):
        lineToBePrinted = ''
        for j in range(currentWidth):
            lineToBePrinted += chr(matrix[i][j])
        print(lineToBePrinted)


def prepareHeader(height, width):

    header = np.array([[' ']*width]*height)

    header[0] = prepareLine(80000, width)
    header[1] = prepareLine(20000, width)
    header[2] = prepareLine(10000, width)
    header[3] = prepareLine(8500, width)
    header[4] = prepareLine(6000, width)
    header[5] = prepareLine(4000, width)
    header[6] = prepareLine(2000, width)

    return header


def prepareFlow(width, matrix):

    flow = matrix 

  
    
    
    for j in range(width):
        if (flow[1][j] == '0'):
            if (random.randint(1, 10) != 1):
                flow[0][j] = '0'
            else:
                flow[0][j] = ' '
        
        else:
            if (random.randint(1, 100) == 50 ):
                flow[0][j] = '0'
            else:
                flow[0][j] = ' '

    flow = np.roll(flow, 1, axis=0)


    return flow

def mergeHeaderAndFlow(header, flow, height, width):
    matrix = header
    
    for i in range(height):
        for j in range(width):
            if (matrix[i][j] == ' ' and flow[i][j] == '0'): 
                matrix[i][j] = '0'

    return matrix


def main2():

    # Creating template for matrix;
    currentWidth = width()
    currentHeight = height()
    matrix = np.array([[' ']*width()]*height())
    flow = np.array([[' ']*width()]*height())


    while 1:

        if ((currentHeight != width()) or (currentWidth != height())):
            currentWidth = width()
            currentHeight = height()
            matrix.resize(currentHeight, currentWidth)

        clear()
        

        # matrix = prepareHeader(currentHeight, currentWidth)
        # matrix = prepareFlow(currentWidth, matrix)
        # prepareHeader

        flow = prepareFlow(currentWidth, flow)
        
        matrix = mergeHeaderAndFlow(prepareHeader(currentHeight, currentWidth), flow, currentHeight, currentWidth)

 

        
    
        # print(matrix)
      
        printMatrix(matrix, currentHeight, currentWidth)
        time.sleep(0.01)
        # input()
        
        




main2()

