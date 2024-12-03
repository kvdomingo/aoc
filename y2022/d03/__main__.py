import string

from common import BASE_DIR


def part_1(data: list[str]):
    priorities = []
    for line in data:
        half_length = len(line) // 2
        comp1, comp2 = line[:half_length], line[half_length:]
        for letter in line:
            if letter in comp1 and letter in comp2:
                priorities.append(string.ascii_letters.index(letter) + 1)
                break
    return sum(priorities)


def part_2(data: list[str]):
    priorities = []
    for i in range(0, len(data), 3):
        r1, r2, r3 = data[i], data[i + 1], data[i + 2]
        aggregate = set(r1) | set(r2) | set(r3)
        for letter in aggregate:
            if letter in r1 and letter in r2 and letter in r3:
                priorities.append(string.ascii_letters.index(letter) + 1)
                break
    return sum(priorities)


def main():
    with open(BASE_DIR / "d03" / "input.txt") as f:
        data = [line.strip() for line in f.readlines() if line]

    p1 = part_1(data)
    p2 = part_2(data)
    print(f"{p1=}", f"{p2=}", sep="\n")


if __name__ == "__main__":
    main()
