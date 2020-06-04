 #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    la_min = max(a)
    lb_max = min(b)
    cnt = 0
    lst = []
    
    for j in range(la_min,lb_max+1):
        if j % a[0] == 0:
            lst.append(j)
    lst1 = []
    for  i in lst:
        for j in range(1,len(a)):
            if i % a[j] != 0:
                break
        else:
            lst1.append(i)

    for i in lst1:
        for j in b:
            if j % i != 0:
                break
        else:
            cnt += 1
    return(cnt)  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
  
