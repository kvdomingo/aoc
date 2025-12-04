from aocd.models import Puzzle, User

from common.config import settings

puzzle = Puzzle(
    year=2025,
    day=1,
    user=User(token=settings.AOC_SESSION.get_secret_value()),
)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(settings.BASE_DIR / "y2025/d01/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def part1(data):
    current = 50
    ticks = 0

    for rotation in data.splitlines():
        direction = -1 if rotation[0] == "L" else 1
        amount = int(rotation[1:])
        current = (current + direction * amount) % 100
        if current == 0:
            ticks += 1

    print(f"{ticks=}")
    return ticks


def part2(data):
    pass
