from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=1)


def load_input(is_test: bool = False):
    if is_test:
        with open(BASE_DIR / "y2024/d01/test.txt") as fh:
            input_ = fh.read().strip()
    else:
        input_ = puzzle.input_data

    return [l.strip().split("   ") for l in input_.split("\n")]


def part1(data: list[list[str]]):
    left = []
    right = []
    for l, r in data:
        left.append(int(l))
        right.append(int(r))

    left = sorted(left, reverse=True)
    right = sorted(right, reverse=True)

    diff_sum = 0
    for l, r in zip(left, right, strict=False):
        diff_sum += abs(l - r)

    print(f"{diff_sum=}")
    return diff_sum


def part2(data: list[list[str]]):
    left = []
    right = []
    for l, r in data:
        left.append(int(l))
        right.append(int(r))

    similarity = 0
    for l in left:
        similarity += sum([r for r in right if r == l])

    print(f"{similarity=}")
    return similarity
