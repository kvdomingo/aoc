from itertools import combinations

from aocd.models import Puzzle, User

from common.config import settings

puzzle = Puzzle(
    year=2025,
    day=9,
    user=User(token=settings.AOC_SESSION.get_secret_value()),
)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(settings.BASE_DIR / "y2025/d09/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def part1(data: str):
    reds = [tuple[int, int](int(n) for n in d.split(",")) for d in data.splitlines()]
    largest = 0

    for a, b in combinations(reds, 2):
        width = abs(a[0] - b[0]) + 1
        height = abs(a[1] - b[1]) + 1
        area = width * height
        largest = max(largest, area)

    print(f"{largest=}")
    return largest


def part2(data: str):
    pass
