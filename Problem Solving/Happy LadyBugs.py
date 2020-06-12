#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    lst = list(b)
    flag = 0
    cnt = Counter(lst)

    if cnt.setdefault('_') == None :     # AABBC
        if len(b) > 2: 
            for i in range(1,len(b)-1):

                    if b[i] != b[i-1] and b[i] != b[i+1]:
                        flag = 1
                        break

            return('NO' if flag == 1 else 'YES')
        else:
            if len(b) == 1:
                return 'NO'
            return ('YES' if b[0] == b[1] else 'NO')
    else:
        del cnt['_']
        for i in cnt.values():
            if i <= 1:
                flag = 1
                break
        else:
            flag = 0
        return('YES' if flag == 0 else 'NO')
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
