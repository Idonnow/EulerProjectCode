import sys
import os
from tqdm import tqdm

def CollatzSequence(n):
    counter = 1
    while(n!=1):
        if (n%2 == 0):
            n = n/2
        else :
            n = 3*n+1
        counter += 1
    return counter

longestSequence = 0
longestSequenceNumber = 0
length = 0
for i in tqdm(range(13,1000000,1)):
    length = CollatzSequence(i)
    if(length > longestSequence):
        #print(str(i) + "have " + str(length)+ " sequence long")
        longestSequence = length
        longestSequenceNumber = i
print (str(longestSequenceNumber)+" have "+str(longestSequence)+" sequence long")
