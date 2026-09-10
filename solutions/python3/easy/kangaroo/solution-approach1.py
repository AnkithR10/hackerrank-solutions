# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
# Problem     Number Line Jumps
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 10:41 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    # If the second kangaroo starts ahead and is faster, or if their speeds are equal and they start at different points, they will never meet.
    if v1 <= v2:
        return "NO"
    
    # After 'n' jumps, their positions will be: x1 + n * v1 and x2 + n * v2
    # We want: x1 + n * v1 == x2 + n * v2
    # n * (v1 - v2) == x2 - x1
    # n == (x2 - x1) / (v1 - v2)
    # For 'n' to be a valid number of jumps, the division must have no remainder.
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
