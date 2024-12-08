from itertools import combinations

import numpy as np
from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=8)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(BASE_DIR / "y2024/d08/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def preprocess_data(data: str):
    return [list(line) for line in data.split("\n")]


def distance(x: int, y: int) -> float:
    return abs((x**2 + y**2) ** 0.5)


def part1(data: str):
    matrix = preprocess_data(data)
    len_x = len(matrix[0])
    len_y = len(matrix)
    unique_frequencies = {
        matrix[j][i] for j in range(len_y) for i in range(len_x) if matrix[j][i] != "."
    }
    unique_antinodes = set()

    for freq in unique_frequencies:
        freq_matrix = np.array(
            [
                [1 if matrix[j][i] == freq else 0 for i in range(len_x)]
                for j in range(len_y)
            ],
            dtype=np.float32,
        )
        antenna_where = np.where(freq_matrix == 1)
        antenna_locations = list(zip(antenna_where[1], antenna_where[0], strict=False))

        for j in range(len_y):
            for i in range(len_x):
                for (ax, ay), (bx, by) in combinations(antenna_locations, 2):
                    dist_a = np.sqrt((i - ax) ** 2 + (j - ay) ** 2)
                    angle_a = np.arctan2(j - ay, i - ax)
                    dist_b = np.sqrt((i - bx) ** 2 + (j - by) ** 2)
                    angle_b = np.arctan2(j - by, i - bx)

                    if (
                        max(dist_a, dist_b) == 2 * min(dist_a, dist_b)
                        and angle_a == angle_b
                    ):
                        if not ((i == ax and j == ay) or (i == bx and j == by)):
                            freq_matrix[j][i] = 0.5
                        unique_antinodes.add((i, j))

    count = len(unique_antinodes)
    print(f"{count=}")
    return count


def part2(data: str):
    matrix = preprocess_data(data)
    len_x = len(matrix[0])
    len_y = len(matrix)
    unique_frequencies = {
        matrix[j][i] for j in range(len_y) for i in range(len_x) if matrix[j][i] != "."
    }
    unique_antinodes = set()

    for freq in unique_frequencies:
        freq_matrix = np.array(
            [
                [1 if matrix[j][i] == freq else 0 for i in range(len_x)]
                for j in range(len_y)
            ],
            dtype=np.float32,
        )
        antenna_where = np.where(freq_matrix == 1)
        antenna_locations = list(zip(antenna_where[1], antenna_where[0], strict=False))

        for loc in antenna_locations:
            unique_antinodes.add(loc)

        for j in range(len_y):
            for i in range(len_x):
                for (ax, ay), (bx, by) in combinations(antenna_locations, 2):
                    angle_a = np.arctan2(j - ay, i - ax)
                    angle_b = np.arctan2(j - by, i - bx)

                    if angle_a == angle_b:
                        if not ((i == ax and j == ay) or (i == bx and j == by)):
                            freq_matrix[j][i] = 0.5
                        unique_antinodes.add((i, j))

    count = len(unique_antinodes)
    print(f"{count=}")
    return count
