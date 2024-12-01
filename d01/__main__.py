from common.config import BASE_DIR


def load_input():
    with open(BASE_DIR / "d01/input.txt") as fh:
        return [l.strip().split("   ") for l in fh.readlines()]


def part1():
    data = load_input()

    left = []
    right = []
    for l, r in data:
        left.append(int(l))
        right.append(int(r))

    left = sorted(left, reverse=True)
    right = sorted(right, reverse=True)

    diff_sum = 0
    for l, r in zip(left, right, strict=False):
        diff_sum += abs(l - r)

    print(f"{diff_sum=}")
    return diff_sum


def part2():
    data = load_input()

    left = []
    right = []
    for l, r in data:
        left.append(int(l))
        right.append(int(r))

    similarity = 0
    for l in left:
        similarity += sum([r for r in right if r == l])

    print(f"{similarity=}")
    return similarity


if __name__ == "__main__":
    part1()
    part2()
