from pytest import fixture

from homework05.oop_1 import Homework, Student, Teacher


@fixture()
def setup_instances():
    return (
        Student("First_name_student", "Last_name_student"),
        Teacher("First_name_teacher", "Last_name_teacher"),
        Homework("Text homework", 1),
    )


@fixture()
def setup_functions():
    def func_for_test_1(n):
        """This is test function 1"""
        if n == 3:
            return 6
        return n ** 2

    def func_for_test_2(n):
        """This is test function 2"""
        if n == 3:
            return 6
        return n * 2

    def func_for_test_3(n):
        """This is test function 3"""
        if n == 3:
            return 6
        return 4

    list = [func_for_test_1, func_for_test_2, func_for_test_3]
    return list
