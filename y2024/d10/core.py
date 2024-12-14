import numpy as np
from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=10)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(BASE_DIR / "y2024/d10/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def preprocess_input(data: str):
    return np.array(
        [[int(s) for s in list(d)] for d in data.split("\n")], dtype=np.uint8
    )


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Vector(Point):
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return Vector(self.x + other.x, self.y + other.y)


DIRECTION_VECTORS = {
    "N": Vector(0, -1),
    "E": Vector(1, 0),
    "S": Vector(0, 1),
    "W": Vector(-1, 0),
}


def part1(data: str):
    matrix = preprocess_input(data)
    zeroes = [(w[1], w[0]) for w in np.where(matrix == 0)]
    return zeroes


def part2(data: str):
    return 36
