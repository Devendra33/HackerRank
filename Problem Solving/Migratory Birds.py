#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    lst = [1,2,3,4,5]    
    for i in range(len(lst)):
        lst[i] = arr.count(lst[i])
    mv = max(lst)
    for j in range(len(lst)):
        if lst[j] == mv:
            return (j+1)
            
        
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
