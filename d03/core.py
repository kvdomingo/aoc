import re

from common.config import BASE_DIR


def load_input(is_test: bool = False):
    file = "d03/test.txt" if is_test else "d03/input.txt"

    with open(BASE_DIR / file) as fh:
        return fh.read().strip()


def mul(x: int, y: int) -> int:
    return x * y


def part1(data: str):
    matches = re.findall(r"mul\(\d+,\d+\)", data)

    sum_ = 0
    for match_ in matches:
        # yes, this is very hacky and potentially dangerous
        sum_ += eval(match_)

    print(f"{sum_=}")
    return sum_


def part2(data: str):
    splits = [d.split("don't()") for d in data.split("do()")]

    sum_ = 0
    for split in splits:
        dos = "".join(split[::2])
        matches = re.findall(r"mul\(\d+,\d+\)", dos)
        for match_ in matches:
            sum_ += eval(match_)

    print(f"{sum_=}")
    return sum_
