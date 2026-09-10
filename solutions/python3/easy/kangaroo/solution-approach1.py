# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
# Problem     Number Line Jumps
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 10:41 p.m.
# Technique   algebraic-linear-equation-solver
# Time        O(1)
# Space       O(1)
# Insight     The kangaroos meet if and only if the relative distance between them is perfectly divisible by the difference in their jump velocities, provided the trailing kangaroo is faster.
# Interview   Before: "I could simulate the jumps in a loop until they meet or pass each other." After: "Since the positions follow a linear equation, I can solve for the number of jumps in O(1) time, ensuring the relative velocity is positive and the distance gap is divisible by that velocity."
# Pitfalls    (1) Failing to handle the case where v1 <= v2, which leads to division by zero or incorrect results.  (2) Assuming that any positive integer solution for n is valid without checking if the remainder of (x2 - x1) / (v1 - v2) is zero.  (3) Neglecting the constraint that the trailing kangaroo must be faster to ever close the initial distance gap.
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
