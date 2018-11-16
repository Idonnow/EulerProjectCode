import sys
import os
from tqdm import tqdm

factorial = 1
for i in range(1,100,1):
    factorial*=i
factorialStr = str(factorial)
sum=0
for char in factorialStr:
    sum+= int(char)

print(sum)
