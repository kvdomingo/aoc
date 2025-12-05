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


def part1(data: str):
    current = 50
    zeroes = 0

    for rotation in data.splitlines():
        direction = -1 if rotation[0] == "L" else 1
        amount = int(rotation[1:])
        current = (current + direction * amount) % 100
        if current == 0:
            zeroes += 1

    print(f"{zeroes=}")
    return zeroes


def part2(data: str):
    current = 50
    zeroes = 0

    for rotation in data.splitlines():
        direction = -1 if rotation[0] == "L" else 1
        amount = int(rotation[1:])
        div, mod = divmod(amount, 100)
        zeroes += div

        if direction == 1:
            if current + mod >= 100:
                zeroes += 1
        else:
            if current != 0 and current - mod <= 0:
                zeroes += 1

        current = (current + (direction * mod)) % 100

    print(f"{zeroes=}")
    return zeroes
