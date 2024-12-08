from itertools import product
from operator import add, mul

from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=7)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(BASE_DIR / "y2024/d07/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def preprocess_input(data: str):
    out = []
    for dat in data.split("\n"):
        ans, vals_ = tuple(dat.split(": "))
        out.append({"key": int(ans), "values": [int(v) for v in vals_.split(" ")]})

    return out


def part1(data: str):
    calibrations = preprocess_input(data)
    pool = "+*"
    sum_ = 0

    for calibration in calibrations:
        test_value = calibration["key"]
        for ops in product(pool, repeat=len(calibration["values"]) - 1):
            test_result = calibration["values"][0]
            for i, op in enumerate(ops):
                match op:
                    case "+":
                        operator = add
                    case "*":
                        operator = mul
                    case _:
                        raise ValueError(f"Unknown {op=} in {ops=}")

                test_result = operator(test_result, calibration["values"][i + 1])

            if test_result == test_value:
                sum_ += test_value
                # once we have a working equation, we can skip the rest of the combinations
                break

    print(f"{sum_=}")
    return sum_


def concat(a: int, b: int) -> int:
    return int(f"{a}{b}")


def part2(data: str):
    calibrations = preprocess_input(data)
    pool = ["+", "*", "||"]
    sum_ = 0

    for calibration in calibrations:
        test_value = calibration["key"]
        for ops in product(pool, repeat=len(calibration["values"]) - 1):
            test_result = calibration["values"][0]
            for i, op in enumerate(ops):
                match op:
                    case "+":
                        operator = add
                    case "*":
                        operator = mul
                    case "||":
                        operator = concat
                    case _:
                        raise ValueError(f"Unknown {op=} in {ops=}")

                test_result = operator(test_result, calibration["values"][i + 1])

            if test_result == test_value:
                sum_ += test_value
                # once we have a working equation, we can skip the rest of the combinations
                break

    print(f"{sum_=}")
    return sum_
