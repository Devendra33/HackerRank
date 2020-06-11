#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    lst = []
    num = n
    cnt = 0
    while n != 0:
        n1 = n % 10        
        n = n // 10
        lst.append(n1)
    for i in lst:
        if i == 0:
            pass
        else:
            if num % i == 0:
                cnt += 1
    
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
