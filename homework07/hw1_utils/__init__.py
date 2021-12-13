from enum import Enum


class PureType(Enum):
    STR = str
    INT = int
    BOOL = bool


class EasyIterType(Enum):
    LIST = list
    TUPLE = tuple
    SET = set
