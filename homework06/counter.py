"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """Some code"""
    counter = 0
    origin_init = cls.__init__

    @classmethod
    def get_created_instances(cls):
        return counter

    @classmethod
    def reset_instances_counter(cls):
        nonlocal counter
        ret = counter
        counter = 0
        return ret

    def __init__(self, *args, **kwargs):
        nonlocal counter
        counter += 1
        origin_init(self, *args, **kwargs)

    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)
    setattr(cls, "__init__", __init__)
    return cls


@instances_counter
class User:
    pass


if __name__ == "__main__":

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    a = user.reset_instances_counter()  # 3
    User.get_created_instances()  # 0
