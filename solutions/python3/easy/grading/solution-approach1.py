# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
# Problem     Grading Students
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 10:39 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38:
            remainder = grade % 5
            if remainder >= 3:
                grade += (5 - remainder)
        rounded_grades.append(grade)
    return rounded_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)) + '\n')

    fptr.close()
