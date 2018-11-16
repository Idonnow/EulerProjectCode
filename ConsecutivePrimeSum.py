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

def primeSum(_primeSequence):
    _str = ""
    _maxLen=0
    _maxSum=0
    for i in tqdm(range(0,len(_primeSequence),1)):
        _sum = 0
        _str = "SUM : "
        _len=0
        while (_sum < MAX):
            if (i+_len+1)>len(_primeSequence):
                break
            elif (_sum+_primeSequence[i+_len])<MAX:
                _str = _str + str(_primeSequence[i+_len])
                _str = _str + "+"
                _sum = _sum + _primeSequence[i+_len]
                _len += 1
                if(isPrime(_sum,_primeSequence)):
                    _str = _str + "=" + str(_sum)
                    _str = _str + " --> " + str(_len) + " step"
                    #print(_str)
                    if (_len > _maxLen):
                        _maxLen = _len
                        _maxSum = _sum
            else :
                break
    return (_maxSum)


localPrimeSequence = createPrimeSequence()
print(primeSum(localPrimeSequence))
