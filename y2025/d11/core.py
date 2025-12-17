from functools import cache

from aocd.models import Puzzle, User

from common.config import settings

puzzle = Puzzle(
    year=2025,
    day=11,
    user=User(token=settings.AOC_SESSION.get_secret_value()),
)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(settings.BASE_DIR / "y2025/d11/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def part1(data: str):
    graph = {
        k: set(v.split(" "))
        for k, v in [line.split(": ") for line in data.splitlines()]
    }

    @cache
    def dfs(node: str) -> int:
        total = 0

        if node == "out":
            return 1

        for child in graph.get(node, []):
            total += dfs(child)

        return total

    total = dfs("you")
    print(f"{total=}")
    return total


def part2(data: str):
    pass
