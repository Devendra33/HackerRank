#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    lst = []; lst_ind = []; lst_r_ind = []
    flag = 0
    for i in s:
        lst.append(ord(i))
    lst_r = lst.copy()
    lst_r.reverse()
    for i in range(1,len(lst)):
        lst_ind.append(abs(lst[i] - lst[i-1]))
        lst_r_ind.append(abs(lst_r[i] - lst_r[i-1]))
    for i in range(len(lst_ind)):
        if lst_ind[i] != lst_r_ind[i]:
                flag = 1
    if flag == 1:
        return('Not Funny')
    else:
        return('Funny')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
