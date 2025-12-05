import re

from aocd.models import Puzzle, User

from common.config import settings

puzzle = Puzzle(
    year=2025,
    day=2,
    user=User(token=settings.AOC_SESSION.get_secret_value()),
)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(settings.BASE_DIR / "y2025/d02/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def part1(data: str):
    ranges = data.split(",")
    ranges = [tuple[int, int](int(r) for r in range_.split("-")) for range_ in ranges]
    sum_ = 0

    for range_ in ranges:
        for i in range(range_[0], range_[1] + 1):
            if len(str(i)) % 2 != 0:
                continue

            half = len(str(i)) // 2
            first_half = str(i)[:half]
            second_half = str(i)[half:]
            if first_half == second_half:
                sum_ += i

    print(f"{sum_=}")
    return sum_


def part2(data: str):
    ranges = data.split(",")
    ranges = [tuple[int, int](int(r) for r in range_.split("-")) for range_ in ranges]
    sum_ = 0

    for range_ in ranges:
        for i in range(range_[0], range_[1] + 1):
            match_ = re.fullmatch(r"(\d+)\1+", str(i))
            if match_ is not None:
                sum_ += i

    print(f"{sum_=}")
    return sum_
