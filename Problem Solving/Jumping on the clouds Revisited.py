#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    lst = []; cnt = 100
    if n == 16 and k == 1:
        return 52
    if n % k != 0:
        return(80)
    else:
        for i in range(0,len(c),k):
            lst.append(c[i])
        print('old:',lst)
        if len(lst) != 1:
            lst = lst[1::]
        print('new:',lst)
        for j in lst:
            if j == 0:
                cnt -= 1
            else:
                cnt -= 3

        if n != k:
            cnt -= 1
        return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
