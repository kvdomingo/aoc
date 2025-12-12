from itertools import combinations
from math import (
    dist as distance,
    prod,
)
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
    junctions = [
        tuple[int, int, int](map(int, line.split(","))) for line in data.splitlines()
    ]
    distances = {(a, b): distance(a, b) for a, b in combinations(junctions, 2)}
    distances = dict(sorted(distances.items(), key=lambda d: d[1]))
    closest_junction_pairs = list(distances.keys())[:1000]

    circuit_junction_lut: dict[int, set[tuple[int, int, int]]] = {}
    junction_circuit_lut: dict[tuple[int, int, int], int] = {}
    next_circuit_id = 0

    for a, b in closest_junction_pairs:
        circuit_a = junction_circuit_lut.get(a, None)
        circuit_b = junction_circuit_lut.get(b, None)

        if circuit_a is None and circuit_b is None:
            new_circuit = next_circuit_id
            next_circuit_id += 1
            junction_circuit_lut[a] = junction_circuit_lut[b] = new_circuit
            circuit_junction_lut[new_circuit] = {a, b}
        elif circuit_a is None:
            assert circuit_b is not None
            junction_circuit_lut[a] = circuit_b
            circuit_junction_lut[circuit_b].add(a)
        elif circuit_b is None:
            assert circuit_a is not None
            junction_circuit_lut[b] = circuit_a
            circuit_junction_lut[circuit_a].add(b)
        else:
            if circuit_a != circuit_b:
                circuit_junction_lut[circuit_a].update(circuit_junction_lut[circuit_b])
                for junc in circuit_junction_lut[circuit_b]:
                    junction_circuit_lut[junc] = circuit_a
                del circuit_junction_lut[circuit_b]

    pp = PrettyPrinter(indent=2)
    sorted_circuits = sorted(
        circuit_junction_lut.values(), key=lambda v: len(v), reverse=True
    )
    print("sorted_circuits")
    pp.pprint(sorted_circuits)
    largest_circuits = sorted_circuits[:3]
    size = prod(len(c) for c in largest_circuits)
    print(f"{size=}")
    return size


def part2(data: str):
    pass
