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
        if (
            bank.count(highest_battery) == 1
            and bank.index(highest_battery) == len(bank) - 1
        ):
            highest_battery = sorted_bank_unique[1]

        if bank.count(highest_battery) == 1:
            highest_battery_idx = bank.index(highest_battery)
            next_highest_battery = max(bank[highest_battery_idx + 1 :])
            highest_joltage = highest_battery * 10 + next_highest_battery
        else:
            highest_battery_positions = [
                i for i, x in enumerate(bank) if x == highest_battery
            ]
            for position in highest_battery_positions:
                if position + 1 >= len(bank):
                    continue

                subbank = bank[position + 1 :]
                sorted_subbank_unique = sorted(set(subbank), reverse=True)
                sub_highest_battery = sorted_subbank_unique[0]
                sub_highest_joltage = highest_battery * 10 + sub_highest_battery
                if sub_highest_joltage > highest_joltage:
                    highest_joltage = sub_highest_joltage

        total += highest_joltage

    print(f"{total=}")
    return total


def part2(data: str):
    banks = [[int(s) for s in list(split)] for split in data.splitlines()]
    total = 0

    for bank in banks:
        highest_joltage = 0
        start_idx = 0

        for i in range(12):
            subbank = bank[start_idx : len(bank) - (12 - i) + 1]
            highest_battery = max(subbank)
            start_idx += subbank.index(highest_battery) + 1
            highest_joltage += highest_battery * 10 ** (12 - i - 1)

        total += highest_joltage

    print(f"{total=}")
    return total
