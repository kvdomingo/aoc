import re

from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=3)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(BASE_DIR / "y2024/d03/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def mul(x: int, y: int) -> int:
    return x * y


def part1(data: str):
    matches = re.findall(r"mul\(\d+,\d+\)", data)

    sum_ = 0
    for match_ in matches:
        # yes, this is very hacky and dangerous
        sum_ += eval(match_)

    print(f"{sum_=}")
    return sum_


def part2(data: str):
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)

    sum_ = 0
    do = True
    for match_ in matches:
        if match_ == "do()":
            do = True
        elif match_ == "don't()":
            do = False
        elif do:
            sum_ += eval(match_)

    print(f"{sum_=}")
    return sum_
