"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k]
     + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from collections import defaultdict
from itertools import product
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    sums = defaultdict(int)
    for pair in product(a, b):
        sums[sum(pair)] += 1
    counter = 0
    for pair in product(c, d):
        if -sum(pair) in sums:
            counter += sums[-sum(pair)]
    return counter
