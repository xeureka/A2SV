# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count = 0

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] < a[i]:
                a[i] = a[i]+a[j]
                a[j] = a[i]-a[j]
                a[i] = a[i] - a[j]
                count += 1

    print(f'Array is sorted in {count} swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
