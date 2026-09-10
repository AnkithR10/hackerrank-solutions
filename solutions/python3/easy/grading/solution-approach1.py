# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
# Problem     Grading Students
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 10:39 p.m.
# Technique   modulo-arithmetic-conditional-rounding
# Time        O(n)
# Space       O(n)
# Insight     The algorithm iterates through each grade, applying the rounding rule only if the grade is at least 38 and the difference to the next multiple of five is less than three.
# Interview   Before: "I would check every grade and manually calculate the next multiple of five." After: "I implemented a O(n) solution using modulo arithmetic to identify the distance to the next multiple of five, ensuring grades below 38 remain unchanged as per the policy."
# Pitfalls    (1) Failing to account for the grade threshold of 38, which prevents rounding for failing grades that would otherwise meet the distance criteria.  (2) Incorrectly rounding grades where the difference to the next multiple of five is exactly 3, as the rule requires the difference to be strictly less than 3.
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
