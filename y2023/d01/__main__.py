from pathlib import Path

with open(Path(__file__).parent / "input.txt") as f:
    data: list[str] = [f.strip() for f in f.readlines() if len(f) > 0]


def part1():
    sum_ = 0
    for line in data:
        calibration = ""
        for char in line:
            if char.isnumeric():
                calibration += char
                break
        for char in reversed(line):
            if char.isnumeric():
                calibration += char
                break
        sum_ += int(calibration)

    return sum_


def part2():
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
    }

    sum_ = 0
    for line in data:
        calibrations = {}
        for i, char in enumerate(line):
            if char.isnumeric():
                calibrations[i] = int(char)

        for number in numbers.keys():
            try:
                calibrations[line.index(number)] = numbers[number]
            except ValueError:
                continue

        calibration = 10 * calibrations[min(calibrations.keys())]
        calibration += calibrations[max(calibrations.keys())]
        sum_ += calibration

    return sum_


def main():
    print(f"{part1()=}", f"{part2()=}", sep="\n")


if __name__ == "__main__":
    main()
