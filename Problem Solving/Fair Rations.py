#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(arr):
    
    total = 0
    a = None
    flips = 0
    for i in range(len(arr)):
        if arr[i]%2 and a == None:
            total += 1
            a = i
        elif arr[i]%2:
            total += 1
            flips += i - a
            a = None             
    return 'NO' if total%2 else flips * 2
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
