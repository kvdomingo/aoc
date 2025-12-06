from aocd.models import Puzzle, User

from common.config import settings

puzzle = Puzzle(
    year=2025,
    day=4,
    user=User(token=settings.AOC_SESSION.get_secret_value()),
)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(settings.BASE_DIR / "y2025/d04/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


DIRECTIONS_MATRIX = {
    "NW": (-1, -1),
    "N": (0, -1),
    "NE": (1, -1),
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0),
}


def is_removable(grid: list[list[str]], x: int, y: int) -> bool:
    surrounding = 0
    for dx, dy in DIRECTIONS_MATRIX.values():
        nx = x + dx
        ny = y + dy
        if 0 <= nx < len(grid[y]) and 0 <= ny < len(grid):
            if grid[ny][nx] == "@":
                surrounding += 1

        if surrounding >= 4:
            return False

    return True


def part1(data: str):
    grid = [list(row) for row in data.splitlines()]
    total = sum(
        [
            is_removable(grid, x, y)
            for y in range(len(grid))
            for x in range(len(grid[y]))
            if grid[y][x] == "@"
        ]
    )
    print(f"{total=}")
    return total


def part2(data: str):
    grid = [list(row) for row in data.splitlines()]
    total = 0
    removables = []

    while True:
        removables = [
            (x, y)
            for y in range(len(grid))
            for x in range(len(grid[y]))
            if grid[y][x] == "@" and is_removable(grid, x, y)
        ]
        total += len(removables)

        if len(removables) == 0:
            break

        grid = [
            ["." if (x, y) in removables else grid[y][x] for x in range(len(grid[y]))]
            for y in range(len(grid))
        ]

    print(f"{total=}")
    return total
