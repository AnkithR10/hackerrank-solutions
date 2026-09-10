# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
# Problem     Apple and Orange
# Difficulty  Easy
# Subdomain   Implementation
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 10:40 p.m.
# ──────────────────────────────────────────────────

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0
    
    for apple in apples:
        landing_position = a + apple
        if s <= landing_position <= t:
            apple_count += 1
            
    for orange in oranges:
        landing_position = b + orange
        if s <= landing_position <= t:
            orange_count += 1
            
    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
