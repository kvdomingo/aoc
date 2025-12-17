from functools import cache
from typing import Literal

from aocd.models import Puzzle, User

from common.config import settings

puzzle = Puzzle(
    year=2025,
    day=11,
    user=User(token=settings.AOC_SESSION.get_secret_value()),
)


def load_input(is_test: bool = False, part: Literal[1, 2] | None = None) -> str:
    if is_test:
        if part is None:
            raise ValueError("`part` is required")

        with open(settings.BASE_DIR / f"y2025/d11/test_part{part}.txt") as fh:
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
    graph = {
        k: set(v.split(" "))
        for k, v in [line.split(": ") for line in data.splitlines()]
    }

    @cache
    def dfs(node: str, *, visited_dac=False, visited_fft=False) -> int:
        total = 0

        if node == "out" and visited_dac and visited_fft:
            return 1

        for child in graph.get(node, []):
            total += dfs(
                child,
                visited_dac=visited_dac or node == "dac",
                visited_fft=visited_fft or node == "fft",
            )

        return total

    total = dfs("svr")
    print(f"{total=}")
    return total
