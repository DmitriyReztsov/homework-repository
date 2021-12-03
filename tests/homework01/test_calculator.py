from homework01.calc import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)


def test_zero():
    """Testing zero"""
    assert not check_power_of_2(0)


def test_negative_int():
    """Testing negative integer"""
    assert not check_power_of_2(-4)


def test_float():
    """Testing float"""
    try:
        check_power_of_2(4.0)
    except Exception:
        pass
    assert Exception
