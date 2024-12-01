from common.config import BASE_DIR


def main():
    with open(BASE_DIR / "d01/input.txt") as fh:
        data = [l.strip().split("   ") for l in fh.readlines()]

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

    print(diff_sum)
    return diff_sum


if __name__ == "__main__":
    main()
