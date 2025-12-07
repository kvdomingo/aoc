from aocd.models import Puzzle, User

from common.config import settings

puzzle = Puzzle(
    year=2025,
    day=7,
    user=User(token=settings.AOC_SESSION.get_secret_value()),
)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(settings.BASE_DIR / "y2025/d07/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def part1(data: str):
    grid = data.splitlines()
    beams = {grid[0].index("S")}
    splits = 0

    for y in range(len(grid)):
        next_beams = set()
        for x in beams:
            if grid[y][x] == "^":
                splits += 1
                if x > 0:
                    next_beams.add(x - 1)
                if x < len(grid[y]) - 1:
                    next_beams.add(x + 1)
            else:
                next_beams.add(x)
        beams = next_beams

    print(f"{splits=}")
    return splits


def part2(data: str):
    pass
