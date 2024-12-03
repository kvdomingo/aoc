from common import BASE_DIR


def main():
    data = []
    totals = []
    with open(BASE_DIR / "d01" / "input.txt") as f:
        raw = f.read()

    this_elf = []
    for line in raw.split("\n"):
        ls = int(line.strip() or 0)
        if not ls:
            data.append(this_elf)
            totals.append(sum(this_elf))
            this_elf = []
            continue
        this_elf.append(ls)

    print("Top 1:", max(totals))

    top_n = 3
    totals_copy = [*totals]
    top_n_totals = []
    for _ in range(top_n):
        top_n_totals.append(totals_copy.pop(totals_copy.index(max(totals_copy))))

    print("Top 3:", sum(top_n_totals))


if __name__ == "__main__":
    main()
