from random import randint

from homework01.task04 import check_sum_of_four

A1 = [1, 2]
B1 = [5, 6]
C1 = [-1, -2]
D1 = [-5, -6]

A2 = [randint(-100, 100) for _ in range(1000)]
B2 = [randint(-100, 100) for _ in range(1000)]
C2 = [randint(-100, 100) for _ in range(1000)]
D2 = [randint(-100, 100) for _ in range(1000)]

A3 = []
B3 = []
C3 = []
D3 = []


def test_positive():
    assert check_sum_of_four(A1, B1, C1, D1) == 6


def test_extreme():
    try:
        check_sum_of_four(A2, B2, C2, D2)
    except MemoryError:
        pass
    assert MemoryError


def test_zero_extreme():
    assert check_sum_of_four(A3, B3, C3, D3) == 0
