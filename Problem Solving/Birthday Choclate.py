#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    # d selects bday date means sum
    # m selects bday month means square to be to be selected.abs
    # s contains the choclate bar  [1, 2, 1, 4, 2, 7, 8, 9]
    # 2 loops are required          0  1  2  3  4  5  6  7
    if len(s) > 1:
        cnt1 = 0
        for i in range(len(s)-m+1):
            cnt = 0
            for j in range(i,i+m):
                cnt += s[j]
            
            if cnt == d:
                cnt1 += 1
        return (cnt1)

    elif len(s) == 1:
        if s[0] == d:
            return (1)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
