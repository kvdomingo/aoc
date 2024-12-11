import re

from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=9)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(BASE_DIR / "y2024/d09/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def preprocess_data(data: str):
    return [int(s) for s in data]


NON_CONTIGUOUS_PATTERN = re.compile(r"\d\.+\d")


def part1(data: str):
    map_ = preprocess_data(data)

    block: list[str | int] = []
    free_idx: list[int] = []
    for i, m in enumerate(map_):
        if i % 2 == 0:
            block.extend([i // 2] * m)
        else:
            free_idx.extend([len(block) + n for n in range(m)])
            block.extend(["."] * m)

    for i in free_idx:
        if not re.search(NON_CONTIGUOUS_PATTERN, "".join([str(b) for b in block])):
            # no more non-contiguous free space; end
            break

        last_non_empty_idx = next(
            (i for i in range(len(block) - 1, -1, -1) if block[i] != "."), None
        )
        if last_non_empty_idx is not None:
            block[i] = block[last_non_empty_idx]
            block[last_non_empty_idx] = "."

    checksum = 0
    for i, b in zip(range(len(block)), block, strict=True):
        if b != ".":
            checksum += i * b

    print(f"{checksum=}")
    return checksum


def part2(data: str):
    return 1928
