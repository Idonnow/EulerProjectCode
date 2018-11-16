import sys
import os
from tqdm import tqdm

def divisor(n):
    counter=0
    for j in range(1,n+1,1):
        modulo = n % j
        #print("Div " + str(j)+" : "+str(n)+" : "+str(modulo))
        if (modulo==0):
            counter+=1
    return(counter)

i=1
_sum = 0
lastMaxDiv=0
while(True):
    _sum = _sum + i
    _divisor = divisor(_sum)
    print(str(i) + " : "+str(_sum)+" : "+str(_divisor),end="\r")
    if (lastMaxDiv<_divisor):
        lastMaxDiv = _divisor
        print(str(i) + " : "+str(_sum)+" : "+str(_divisor))
    if(_divisor>=500):
        print(_sum)
        break
    i+=1
