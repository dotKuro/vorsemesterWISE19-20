from collections import namedtuple
from enum import Enum, auto

Object = namedtuple('Object', 'x y')


class ObjectName(Enum):
    HEAD = auto()
    TAIL = auto()
    APPLE = auto()
    WALL = auto()
    FREE = auto()
