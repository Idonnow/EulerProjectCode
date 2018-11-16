import sys
import os
from tqdm import tqdm

number = pow(2,1000)
print(number)
string = str(number)
print(string)
_sum = 0
for char in tqdm(string):
    _sum += int(char)
print(_sum)
