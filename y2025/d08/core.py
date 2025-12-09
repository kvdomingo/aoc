from math import prod
from pprint import PrettyPrinter

from aocd.models import Puzzle, User

from common.config import settings

puzzle = Puzzle(
    year=2025,
    day=8,
    user=User(token=settings.AOC_SESSION.get_secret_value()),
)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(settings.BASE_DIR / "y2025/d08/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def part1(data: str):
    vectors = [
        tuple[int, int, int](map(int, line.split(","))) for line in data.splitlines()
    ]
    circuit_junction_lut: dict[int, set[tuple[int, int, int]]] = {}
    junction_circuit_lut: dict[tuple[int, int, int], int] = {}

    for i, vec in enumerate(vectors):
        new_circuit = i
        circuit_junction_lut[new_circuit] = {vec}
        junction_circuit_lut[vec] = new_circuit

    for a in range(len(vectors)):
        min_dist = float("inf")
        closest = None
        for b in range(a + 1, len(vectors)):
            dist = sum((vectors[a][i] - vectors[b][i]) ** 2 for i in range(3))
            if dist < min_dist:
                min_dist = dist
                closest = vectors[b]

        if closest is None:
            continue

        circuit_a = junction_circuit_lut[vectors[a]]
        circuit_b = junction_circuit_lut[closest]
        if circuit_a != circuit_b:
            circuit_junction_lut[circuit_a].update(circuit_junction_lut[circuit_b])
            for vec in circuit_junction_lut[circuit_b]:
                junction_circuit_lut[vec] = circuit_a
            del circuit_junction_lut[circuit_b]

    pp = PrettyPrinter(indent=2)
    print("circuit_junction_lut")
    pp.pprint(circuit_junction_lut)
    print("junction_circuit_lut")
    pp.pprint(junction_circuit_lut)

    sorted_circuits = sorted(
        circuit_junction_lut.values(), key=lambda v: len(v), reverse=True
    )
    largest_circuits = sorted_circuits[:3]
    size = prod(len(c) for c in largest_circuits)
    print(f"{size=}")
    return size


def part2(data: str):
    pass
