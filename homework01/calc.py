def check_power_of_2(a: int) -> bool:
    return a > 0 and not (bool(a & (a - 1)))
