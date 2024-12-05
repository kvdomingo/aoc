from math import ceil

from aocd.models import Puzzle

from common.config import BASE_DIR

puzzle = Puzzle(year=2024, day=5)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(BASE_DIR / "y2024/d05/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def preprocess_data(data: str):
    sec1, sec2 = data.split("\n\n")
    rules: list[tuple[int, ...]] = [
        tuple(int(s) for s in sec.split("|")) for sec in sec1.split("\n")
    ]
    updates: list[list[int]] = [
        [int(s) for s in sec.split(",")] for sec in sec2.split("\n")
    ]
    return rules, updates


def part1(data: str):
    rules, updates = preprocess_data(data)

    mids = 0
    correct_updates = []
    for update in updates:
        rule_evals = 0
        for i in range(len(update) - 1):
            for r in rules:
                if r[0] == update[i] and r[1] == update[i + 1]:
                    rule_evals += 1

            if len(update) - 1 == rule_evals:
                correct_updates.append(update)

    for update in correct_updates:
        arg_mid = int(ceil(len(update) / 2)) - 1
        mid = update[arg_mid]
        mids += mid

    return mids


def part2(data: str):
    pass
