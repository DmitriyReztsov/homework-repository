from homework01.task02 import check_fibonacci


def test_positive_case_list():
    sequence = [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
    ]
    assert check_fibonacci(sequence)


def test_positive_case_tuple():
    sequence = (
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
    )
    assert check_fibonacci(sequence)


def test_negative_case_list():
    sequence = [
        0,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
    ]
    assert not check_fibonacci(sequence)


def test_negative_start_int():
    sequence = [
        0,
        -1,
        -1,
        -2,
        -3,
        -5,
        -8,
        -13,
        -21,
        -34,
        -55,
        -89,
        -144,
        -233,
        -377,
        -610,
        -987,
        -1597,
        -2584,
        -4181,
        -6765,
    ]
    assert not check_fibonacci(sequence)


def test_slice_tuple():
    sequence = (3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610)
    assert check_fibonacci(sequence)


def test_slice_negative_start():
    sequence = (-3, 5, 2, 7, 9, 16, 25)
    assert not check_fibonacci(sequence)


def test_3_elements_like_fibonacci():
    sequence = (2, 7, 9)
    assert check_fibonacci(sequence) is False


def test_2_elements():
    sequence = (2, 7)
    assert check_fibonacci(sequence) is False
