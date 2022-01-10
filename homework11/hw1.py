"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __new__(cls, class_name, parents, attributes):
        cls.keys = set(attributes[f"_{class_name}__keys"])
        return super().__new__(cls, class_name, parents, attributes)

    def __getattr__(self, key):
        if key in self.keys:
            return key
        raise AttributeError(f"type object {self} has no attribute {key}")


def SimplifiedEnum2(class_name, parents, attributes):
    myattributes = {}
    for name, attr in attributes.items():
        if f"{class_name}__key" in name:
            for at in attr:
                myattributes[at] = at
        myattributes[name] = attr

    return type(class_name, parents, myattributes)
