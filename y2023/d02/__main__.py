from pathlib import Path

with open(Path(__file__).parent / "input.txt") as f:
    data: list[str] = [l for l in f.readlines() if len(l) > 0]


def part1():
    red_limit = 12
    blue_limit = 14
    green_limit = 13

    def do(line: str) -> int | None:
        game, rest = line.split(": ")
        game_number = int(game.split()[-1])
        for subset in rest.split("; "):
            for set_ in subset.split(", "):
                count, color = set_.split()
                if (
                    (color == "red" and int(count) > red_limit)
                    or (color == "green" and int(count) > green_limit)
                    or (color == "blue" and int(count) > blue_limit)
                ):
                    return None
        return game_number

    sum_ = 0
    for line in data:
        if (number := do(line)) is not None:
            sum_ += number
    return sum_


def main():
    print(f"{part1()=}", sep="\n")


if __name__ == "__main__":
    main()
