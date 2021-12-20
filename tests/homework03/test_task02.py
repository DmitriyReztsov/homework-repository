import time

from homework03.task02.task02 import speedy_calculator


def test_speed():
    start_time = time.time()
    speedy_calculator(501)  # to arrange range from 0 to 500
    total_time = time.time() - start_time
    assert total_time <= 60
