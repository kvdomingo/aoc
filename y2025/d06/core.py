import re
from math import prod
from typing import cast

from aocd.models import Puzzle, User

from common.config import settings

puzzle = Puzzle(
    year=2025,
    day=6,
    user=User(token=settings.AOC_SESSION.get_secret_value()),
)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(settings.BASE_DIR / "y2025/d06/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def part1(data: str):
    full_grid = [
        [int(s) if s.isnumeric() else s for s in re.split(r"\s+", line.strip())]
        for line in data.splitlines()
    ]
    grid = cast(list[list[int]], full_grid[:-1])
    operations = full_grid[-1]
    results = []

    for i, operation in enumerate(operations):
        op = sum if operation == "+" else prod
        results.append(op([row[i] for row in grid]))

    result = sum(results)
    print(f"{result=}")
    return result


def part2(data: str):
    pass
