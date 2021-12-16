from homework06.counter import instances_counter


@instances_counter
class TestClass:
    def __init__(self, check):
        self.check = check


def test_counter():
    assert TestClass.get_created_instances() == 0

    test_instance_1 = TestClass("check 1")
    assert TestClass.get_created_instances() == 1
    assert test_instance_1.get_created_instances() == 1
    assert test_instance_1.check == "check 1"

    test_instance_2 = TestClass("check 2")
    assert TestClass.get_created_instances() == 2
    assert test_instance_1.get_created_instances() == 2
    assert test_instance_2.get_created_instances() == 2
    assert test_instance_2.check == "check 2"

    test_instance_3 = TestClass("check 3")
    assert TestClass.get_created_instances() == 3
    assert test_instance_1.get_created_instances() == 3
    assert test_instance_2.get_created_instances() == 3
    assert test_instance_3.get_created_instances() == 3
    assert test_instance_3.check == "check 3"

    TestClass.reset_instances_counter()
    assert TestClass.get_created_instances() == 0
    assert test_instance_3.get_created_instances() == 0
