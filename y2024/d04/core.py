from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=4)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(BASE_DIR / "y2024/d04/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def part1(data: str):
    matrix = [list(d) for d in data.split("\n")]
    len_x = len(matrix[0])
    len_y = len(matrix)
    find_word = "XMAS"

    def check_direction(x, y, dx, dy):
        for i in range(len(find_word)):
            nx = x + i * dx
            ny = y + i * dy

            if 0 <= nx < len_x and 0 <= ny < len_y and matrix[ny][nx] == find_word[i]:
                continue
            else:
                return False

        return True

    directions = [
        (0, 1),  # south
        (1, 0),  # east
        (0, -1),  # north
        (-1, 0),  # west
        (1, 1),  # southeast
        (1, -1),  # northeast
        (-1, 1),  # northwest
        (-1, -1),  # southwest
    ]

    count = 0
    for y in range(len_y):
        for x in range(len_x):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    count += 1

    print(f"{count=}")
    return count


def part2(data: str):
    matrix = [list(d) for d in data.split("\n")]
    len_x = len(matrix[0])
    len_y = len(matrix)
    count = 0

    for y in range(len_y):
        for x in range(len_x):
            if x - 1 < 0 or y - 1 < 0 or x + 1 == len_x or y + 1 == len_x:
                # boundary condition
                continue

            if matrix[y][x] == "A" and (
                all(
                    [
                        matrix[y - 1][x - 1] == "M",  # M M
                        matrix[y - 1][x + 1] == "M",  #  A
                        matrix[y + 1][x - 1] == "S",  # S S
                        matrix[y + 1][x + 1] == "S",
                    ]
                )
                or all(
                    [
                        matrix[y - 1][x - 1] == "S",  # S S
                        matrix[y - 1][x + 1] == "S",  #  A
                        matrix[y + 1][x - 1] == "M",  # M M
                        matrix[y + 1][x + 1] == "M",
                    ]
                )
                or all(
                    [
                        matrix[y - 1][x - 1] == "M",  # M S
                        matrix[y - 1][x + 1] == "S",  #  A
                        matrix[y + 1][x - 1] == "M",  # M S
                        matrix[y + 1][x + 1] == "S",
                    ]
                )
                or all(
                    [
                        matrix[y - 1][x - 1] == "S",  # S M
                        matrix[y - 1][x + 1] == "M",  #  A
                        matrix[y + 1][x - 1] == "S",  # S M
                        matrix[y + 1][x + 1] == "M",
                    ]
                )
            ):
                count += 1

    print(f"{count=}")
    return count
