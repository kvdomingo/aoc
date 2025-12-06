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


def load_input(is_test: bool = False, strip_extra_whitespace: bool = True) -> str:
    if is_test:
        with open(settings.BASE_DIR / "y2025/d06/test.txt") as fh:
            read = fh.read()
            if strip_extra_whitespace:
                read = read.strip()
            return read

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
    grid = [[r.strip() for r in list(line)] for line in data.splitlines()]
    row_size = len(grid[0])
    col_size = len(grid)
    results = []

    sub_problem = ""
    problem = list[int]()
    for x in range(row_size - 1, -1, -1):
        # concat all numbers in column except last row
        for y in range(col_size - 1):
            sub_problem += grid[y][x]

        # entire column is empty, skip to next iteration
        if sub_problem == "":
            continue

        # append to problem and reset sub_problem string
        problem.append(int(sub_problem))
        sub_problem = ""

        # if last row has no operator, skip to next iteration
        if not grid[-1][x]:
            continue

        # compute the problem
        op = sum if grid[-1][x] == "+" else prod
        results.append(op(problem))
        problem = list[int]()

    result = sum(results)
    print(f"{result=}")
    return result
