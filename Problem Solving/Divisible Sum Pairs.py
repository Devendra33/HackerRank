#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    cnt1 = 0
    for i in range(n):
                
        for j in range(n):
            cnt = 0
            if i < j:
               cnt += ar[i] + ar[j]
               if cnt % k == 0:
                   cnt1 += 1
    return (cnt1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
