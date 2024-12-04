from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=4)

FIND_WORD = "XMAS"


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(BASE_DIR / "y2024/d04/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def flatten_diagonally(matrix: list[list]):
    out = []
    len_x = len(matrix[0])
    len_y = len(matrix)

    for i in range(len_x + len_y - 1):
        diag = []
        for j in range(max(0, i - len_y + 1), min(i + 1, len_x)):
            diag.append(matrix[j][i - j])
        out.extend(diag)

    for i in range(1, len_y):
        diag = []
        for j in range(min(len_x, i + 1)):
            diag.append(matrix[j][i - j])
        out.extend(diag)

    return out


def flip_horizontal(matrix: list[list]):
    len_y = len(matrix)
    out = []

    for j in range(len_y):
        out.append(matrix[j][::-1])

    return out


def part1(data: str):
    matrix = [list(d) for d in data.split("\n")]
    matrix_f = flip_horizontal(matrix)
    len_x = len(matrix[0])
    len_y = len(matrix)

    horizontal = [r for row in matrix for r in row]
    reverse_horizontal = horizontal[::-1]
    vertical = [matrix[j][i] for i in range(len_x) for j in range(len_y)]
    reverse_vertical = vertical[::-1]

    diagonal_ne = flatten_diagonally(matrix)
    diagonal_sw = diagonal_ne[::-1]

    diagonal_se = flatten_diagonally(matrix_f)
    diagonal_nw = diagonal_se[::-1]

    count = 0
    for flat in [
        horizontal,
        reverse_horizontal,
        vertical,
        reverse_vertical,
        diagonal_ne,
        diagonal_sw,
        diagonal_se,
        diagonal_nw,
    ]:
        count += "".join(flat).count(FIND_WORD)

    print(f"{count=}")
    return count


def part2(data: str):
    pass
