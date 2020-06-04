#!/bin/python3

import math
import os
import random
import re
import sys
def counter(fruit,s,t):
    cnt = 0
    for i in fruit:
        if i>=s and i<=t:
            cnt += 1
    return cnt
    
def countApplesAndOranges(s, t, a, b, apples, oranges):
     
    for i in range(len(apples)):
        apples[i] = apples[i] + a
    
    for j in range(len(oranges)):
        oranges[j] = oranges[j] + b
    
    cnt_app = counter(apples,s,t)
    cnt_oran = counter(oranges,s,t)
    print(f'{cnt_app}\n{cnt_oran} ')
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
