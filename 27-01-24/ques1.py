import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from datetime import datetime

def timeConversion(s):
    # Write your code here
    time_12h = datetime.strptime(s, "%I:%M:%S%p")
    time_24h = time_12h.strftime("%H:%M:%S")
    
    return time_24h


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
