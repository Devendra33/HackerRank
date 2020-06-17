#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    set_lst = list(set(ar))
    lst = []
    for i in set_lst:
        temp = 0
        temp = ar.count(i)
        if temp == 0 or temp == 1:
            temp = 0 
        elif temp % 2 != 0:
            temp -= 1
            temp = temp//2
        elif temp % 2 == 0:
            temp = temp//2
        lst.append(temp)
    return (sum(lst))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
