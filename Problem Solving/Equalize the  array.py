#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the equalizeArray function below.
def equalizeArray(arr):
    cnt = Counter(arr)
    temp = 0  
    for k in cnt.keys():
        if cnt[k] > temp:
            temp =  cnt[k]
            mx = k 
    cnt[mx] = 0
    return (sum(cnt.values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
