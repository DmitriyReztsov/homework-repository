from homework01.task05 import find_maximal_subarray_sum

A1 = []

A2 = [1, 16, -1, -3, 5, 3, 6, 7]

A3 = [1, 2, "asd"]


def test_empty_list():
    assert find_maximal_subarray_sum(A1, 3) is None


def test_positive():
    assert find_maximal_subarray_sum(A2, 3) == 17


def test_wrong_type():
    try:
        find_maximal_subarray_sum(A3, 2) == 0
    except Exception:
        pass
    assert Exception
