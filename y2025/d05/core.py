from aocd.models import Puzzle, User

from common.config import settings

puzzle = Puzzle(
    year=2025,
    day=5,
    user=User(token=settings.AOC_SESSION.get_secret_value()),
)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(settings.BASE_DIR / "y2025/d05/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def part1(data: str):
    lines = data.splitlines()
    blank_idx = lines.index("")
    fresh_ranges = [
        tuple(int(r) for r in line.split("-")) for line in lines[:blank_idx]
    ]
    available_ids = [int(line) for line in lines[blank_idx + 1 :]]
    fresh_ranges = [range(start, end + 1) for start, end in fresh_ranges]

    fresh = 0
    for available_id in available_ids:
        for range_ in fresh_ranges:
            if available_id in range_:
                fresh += 1
                break

    print(f"{fresh=}")
    return fresh


def part2(data: str):
    pass
