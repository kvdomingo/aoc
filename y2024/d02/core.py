from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=2)


def load_input(is_test: bool = False) -> list[list[int]]:
    if is_test:
        with open(BASE_DIR / "y2024/d02/test.txt") as fh:
            input_ = fh.read().strip()
    else:
        input_ = puzzle.input_data

    data = []
    for line in input_.split("\n"):
        data.append([int(l) for l in line.strip().split(" ")])

    return data


def is_row_safe(row: list[int]):
    unidirectional = all(r < 0 for r in row) or all(r > 0 for r in row)
    within_1_3 = all(1 <= abs(r) <= 3 for r in row)
    return unidirectional and within_1_3


def compute_diff(row: list[int]):
    return [row[i + 1] - row[i] for i in range(len(row) - 1)]


def part1(data: list[list[int]]):
    diffs: list[list[int]] = []
    for row in data:
        diffs.append([row[i + 1] - row[i] for i in range(len(row) - 1)])

    safes = sum([is_row_safe(row) for row in diffs])

    print(f"{safes=}")
    return safes


def part2(data: list[list[int]]):
    safes = 0
    for row in data:
        diff = compute_diff(row)

        if is_row_safe(diff):
            safes += 1
            continue

        for i in range(len(row)):
            tmp_row = row.copy()
            tmp_row.pop(i)
            diff = compute_diff(tmp_row)
            if is_row_safe(diff):
                safes += 1
                break

    print(f"{safes=}")
    return safes
