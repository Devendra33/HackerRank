#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    cnt_min = 0
    arr.sort()
    for i in range(0, (len(arr)-1)):
        cnt_min +=  arr[i]
    print(f'{cnt_min} ',end = "")
    arr.pop(0)
    print(sum(arr))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
