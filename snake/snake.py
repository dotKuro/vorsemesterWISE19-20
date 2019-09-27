from enum import Enum, auto

from object import Object, ObjectName


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class Snake():

    def __init__(self, head):
        self.head = head
        self.tail = []
        self.direction = Direction.UP

    def move(self, apple, x_max, y_max):
        self.tail.append(self.head)
        if self.direction == Direction.UP:
            self.head = Object(self.head.x, self.head.y-1)
        elif self.direction == Direction.DOWN:
            self.head = Object(self.head.x, self.head.y+1)
        elif self.direction == Direction.LEFT:
            self.head = Object(self.head.x-1, self.head.y)
        elif self.direction == Direction.RIGHT:
            self.head = Object(self.head.x+1, self.head.y)

        if self.head == apple:
            return ObjectName.APPLE
        else:
            self.tail.pop(0)
            if self.head.x > x_max or self.head.y > y_max or self.head.x < 0 or self.head.y < 0:
                return ObjectName.WALL
            elif self.head in self.tail:
                return ObjectName.TAIL
            else:
                return ObjectName.FREE
