from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=11)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(BASE_DIR / "y2024/d11/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def preprocess_input(data: str):
    return [int(d) for d in data.split("\n")[0].split(" ")]


def apply_rule(i: int) -> list[int]:
    if i == 0:
        return [1]

    if (len_digits := len(str_i := str(i))) % 2 == 0:
        return [int(str_i[: len_digits // 2]), int(str_i[len_digits // 2 :])]

    return [i * 2024]


def blink(ins: list[int], times: int):
    input_ = ins.copy()
    for _ in range(times):
        input_ = [a for b in input_ for a in apply_rule(b)]

    return input_


def part1(data: str):
    ins = preprocess_input(data)
    out = blink(ins, 25)

    count = len(out)
    print(f"{count=}")
    return count


def part2(data):
    ins = preprocess_input(data)
    out = blink(ins, 75)

    count = len(out)
    print(f"{count=}")
    return count
