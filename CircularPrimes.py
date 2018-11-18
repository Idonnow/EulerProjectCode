import sys
import os
from tqdm import tqdm

MAX = 1000000

def isPrime(_number,_primeSequence=None):
    if _primeSequence is None:
        for i in range(2,_number,1):
            #print(str(_number)+"%"+str(i)+"="+str(_number%i))
            if ((_number%i) == 0):
                return False
        return True
    else:
        for prime in _primeSequence:
            if prime == _number:
                return True
        return False



def createPrimeSequence():
    _primeSequence = []
    for i in tqdm(range(2,int(MAX),1)):
        if isPrime(i):
            _primeSequence.append(i)
    #print(_primeSequence)
    return _primeSequence

def isCircular (_number,_primeSequence):
    if (len(str(_number)))
