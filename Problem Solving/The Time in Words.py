#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    word_time = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','ten','eleven','twelve']
    ind_wt = -13 + h
    # create a dictionary for each and every minute.
    min_time = {0:"o' clock", 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'quarter', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 21:'twenty one', 22:'twenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',29:'twenty nine',30:'half',31:'twenty nine',32:'twenty eight', 33:'twenty seven',34:'twenty six',35:'twenty five',36:'twenty four',37:'twenty three',38:'twenty two',39:'twenty one',40:'twenty',41:'nineteen',42:'eighteen',43:'seventeen',44:'sixteen',45:'quarter',46:'fourteen',47:'thirteen',48:'twelve',49:'eleven',50:'ten',51:'nine',52:'eight',53:'seven',54:'six',55:'five',56:'four',57:'three',58:'two',59:'one' }
    print(m)
    if m == 0:
        return f'{word_time[ind_wt]} {min_time[0]}'
    elif m == 1:
        return f'{min_time[m]} minute past {word_time[ind_wt]}'
    elif m == 15 or m == 30:
        return f'{min_time[m]} past {word_time[ind_wt]}'    
    elif m < 30:
        return f'{min_time[m]} minutes past {word_time[ind_wt]}'
    elif m == 45:
        return f'{min_time[m]} to {word_time[ind_wt + 1]}'
    elif m >= 30:
        return f'{min_time[m]} minutes to {word_time[ind_wt + 1]}'

    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
