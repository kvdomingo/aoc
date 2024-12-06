from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=6)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(BASE_DIR / "y2024/d06/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def preprocess_input(data: str) -> list[list[str]]:
    return [list(s) for s in data.split("\n")]


START_CHAR = "^"


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


class Guard:
    directions = {
        "N": Position(0, -1),
        "E": Position(1, 0),
        "S": Position(0, 1),
        "W": Position(-1, 0),
    }
    heading = list(directions.keys())[0]

    def __init__(self, initial_position: tuple[int, int]):
        self.position = Position(*initial_position)

    def plan_move_forward(self):
        position = self.position + self.directions[self.heading]
        return position

    def commit_move_forward(self):
        self.position += self.directions[self.heading]

    def rotate_clockwise(self):
        self.heading = list(self.directions.keys())[
            (list(self.directions.keys()).index(self.heading) + 1) % 4
        ]


def part1(data: str):
    matrix = preprocess_input(data)
    len_y = len(matrix)
    len_x = len(matrix[0])
    start_pos = next(
        (i, j) for j in range(len_y) for i in range(len_x) if matrix[j][i] == START_CHAR
    )
    guard = Guard(start_pos)

    while True:
        new_pos = guard.plan_move_forward()

        if any([new_pos.x < 0, new_pos.x >= len_x, new_pos.y < 0, new_pos.y >= len_y]):
            # out of bounds
            matrix[guard.position.y][guard.position.x] = "X"
            break

        if matrix[new_pos.y][new_pos.x] == "#":
            # hit obstacle; rotate clockwise
            guard.rotate_clockwise()
            continue

        matrix[guard.position.y][guard.position.x] = "X"
        guard.commit_move_forward()

    flat = "".join(["".join(row) for row in matrix])
    count = flat.count("X")
    print(f"{count=}")
    return count


def part2(data):
    pass
