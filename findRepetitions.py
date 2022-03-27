#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'read_and_find_repetitions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING short_s
#  2. STRING long_s
#

def read_and_find_repetitions(short_s, long_s):
    # Write your code here
    shortLen = len(short_s)
    longLen = len(long_s)
    
    prevMatchIdx = -10
    
    if shortLen == 0 or longLen == 0:
        return 0
    
    left = 0
    right = shortLen
    
    count = 0
    
    while right < longLen:
        word = long_s[left:right]
        if word == short_s:
            if prevMatchIdx != left-shortLen:
                count += 1
                #
            else:
                count -= 1
                prevMatchIdx = left
                
        left += shortLen
        right += shortLen
        
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    short_s = input()

    long_s = input()

    result = read_and_find_repetitions(short_s, long_s)

    fptr.write(str(result) + '\n')

    fptr.close()

short = "AB"
long = "ABCABCABAB"

print(read_and_find_repetitions(short, long))