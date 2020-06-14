#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    # print(a)

    mlen = 0
    for i in range(len(a)-1):
        lst = []
        flag = 0
        for j in range(i+1,len(a)):
            if a[j] - a[i] <= 1:
                if flag  == 0:
                    lst.append(a[i])
                    lst.append(a[j])
                    flag = 1
                else:
                    lst.append(a[j])

            else:
                break
        if mlen < len(lst):
            mlen = len(lst)
    return (mlen)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
