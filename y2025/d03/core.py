from aocd.models import Puzzle, User

from common.config import settings

puzzle = Puzzle(
    year=2025,
    day=3,
    user=User(token=settings.AOC_SESSION.get_secret_value()),
)


def load_input(is_test: bool = False) -> str:
    if is_test:
        with open(settings.BASE_DIR / "y2025/d03/test.txt") as fh:
            return fh.read().strip()

    return puzzle.input_data


def part1(data: str):
    banks = [[int(s) for s in list(split)] for split in data.splitlines()]
    total = 0

    for bank in banks:
        highest_joltage = 0

        sorted_bank_unique = sorted(set(bank), reverse=True)
        highest_battery = sorted_bank_unique[0]
        if bank.index(highest_battery) == len(bank) - 1:
            highest_battery = sorted_bank_unique[1]

        if bank.count(highest_battery) == 1:
            highest_battery_idx = bank.index(highest_battery)
            next_battery = bank[highest_battery_idx + 1]
            highest_joltage = highest_battery * 10 + next_battery
        else:
            for i, battery in enumerate(bank):
                if battery != highest_battery or i + 1 >= len(bank):
                    continue

                next_battery = bank[i + 1]
                current_joltage = battery * 10 + next_battery
                if current_joltage > highest_joltage:
                    highest_joltage = current_joltage

        total += highest_joltage

    print(f"{total=}")
    return total


def part2(data: str):
    pass
