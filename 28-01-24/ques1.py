import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def maxMin(k, arr):
    # Write your code here
    arr.sort()  
  
    min_unfair = float('infinity') 
    
    for i in range(len(arr) - k + 1):
        unfairness = arr[i + k - 1] - arr[i]  
        min_unfair = min(min_unfair, unfairness) 
    return min_unfair

