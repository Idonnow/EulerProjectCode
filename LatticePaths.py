import sys
import os

gridSize = 20

def moveforward(col,line):
    counter = 0
    #print("Call "+str(col)+" : "+str(line))
    if (col != gridSize):
        counter = moveforward(col+1,line)
    if (line != gridSize):
        counter = counter + moveforward(col,line+1)
    if (col == gridSize)and(line == gridSize):
        counter+=1
        #print(counter,end="\r")
    print("Call "+str(col)+" : "+str(line)+" : "+str(counter),end="\r")
    return (counter)

print(moveforward(0,0))
