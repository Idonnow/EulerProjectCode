from decimal import *

from math import sqrt

getcontext().prec = 102


def digitalsum(n):
    sum = 0
    for a in n:
        sum += int(a)
    return sum

total = 0

for a in range(100):
    if not sqrt(a) % 1 == 0:
        ans = str(Decimal(a).sqrt()).replace('.', '')[:100]
        print(a)
        print(digitalsum(ans))
        print("-------")
