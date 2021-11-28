import io
from contextlib import redirect_stdout

from homework05.save_original_info import print_result


def test_decorator(setup_functions):
    for number, pure_func in enumerate(setup_functions):
        func = print_result(pure_func)
        with redirect_stdout(io.StringIO()) as output:
            output = func(2)
        assert output == 4
        assert func.__doc__ == f"This is test function {number + 1}"
        assert func.__name__ == f"func_for_test_{number + 1}"
        assert func.__original_func(3) == 6
