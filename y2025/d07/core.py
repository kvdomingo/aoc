from functools import cache

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

    for y in range(1, len(grid)):
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
    grid = data.splitlines()
    start_x = grid[0].index("S")
    sy = len(grid)
    sx = len(grid[0])

    @cache
    def dfs(x: int, y: int) -> int:
        timelines = 0

        if grid[y][x] == ".":
            if y + 1 >= sy:
                timelines += 1
            else:
                timelines += dfs(x, y + 1)

        if grid[y][x] == "^":
            # Traverse the left branch of a split
            if x > 0:
                timelines += dfs(x - 1, y + 1)

            # Traverse the right branch of a split
            if x < sx - 1:
                timelines += dfs(x + 1, y + 1)

        return timelines

    timelines = dfs(start_x, 2)

    print(f"{timelines=}")
    return timelines
