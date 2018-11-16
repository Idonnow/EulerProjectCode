import sys
import os
from tqdm import tqdm

i=0
numberStr = ""
while(True):
    if (len(numberStr)>=1000001):
        break
    numberStr = numberStr + str(i)
    i+=1

print(numberStr[1])
print(numberStr[10])
print(numberStr[100])
print(numberStr[1000])
print(numberStr[10000])
print(numberStr[100000])
print(numberStr[1000000])
result=int(numberStr[1])
result*=int(numberStr[10])
result*=int(numberStr[100])
result*=int(numberStr[1000])
result*=int(numberStr[10000])
result*=int(numberStr[100000])
result*=int(numberStr[1000000])
print(result)
