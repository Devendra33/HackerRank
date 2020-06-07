#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arr.sort()
    set1 = list(set(arr))
    set1.sort()
    lst = []
    for i in set1:
        lst.append(len(arr))
        cnt = arr.count(i)
        for j in range(cnt):
            arr.remove(i)
        
    return(lst)
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
