#!/bin/python3

import math
import os
import random
import re
import sys
import textwrap
# Complete the kaprekarNumbers function below.

def kaprekarNumbers(p, q):
    # use textwrapper function
    kap_num = []
    for i in range(p,q+1):
        n = i * i
        d = pow(10,len(str(i)))
        split_sum = 0
        while n != 0:
            split_sum += n % d
            n = n // d
        if split_sum == i:
            kap_num.append(i)
    if len(kap_num) == 0:
        print('INVALID RANGE')
    else:
        print(*kap_num)


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
