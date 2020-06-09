#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    dic = {}
    inr = 0
    max_val = 0 
    for i in h:
        dic[chr(97+inr)] = i
        inr += 1
    for j in word:
        if dic[j] > max_val:
            max_val = dic[j]
    return len(word)*max_val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
