"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k]
     + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List

import numpy as np


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    x1, y1, z1, t1 = np.meshgrid(a, b, c, d)
    cl1 = x1 + y1 + z1 + t1
    array = np.extract(cl1 == 0, cl1)
    return len(array)
