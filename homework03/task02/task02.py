import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def speedy_calculator(to_range: int) -> int:
    numbers = [x for x in range(to_range)]
    pool = Pool(processes=to_range)
    result_array = pool.map_async(slow_calculate, numbers).get()
    return sum(result_array)
