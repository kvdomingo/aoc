from enum import IntEnum

from common import BASE_DIR


class Outcome(IntEnum):
    LOSE = 0
    DRAW = 3
    WIN = 6


def part_1(data: list[str]):
    class Play(IntEnum):
        X = 1
        Y = 2
        Z = 3

    outcomes = {
        "A X": Outcome.DRAW,
        "A Y": Outcome.WIN,
        "A Z": Outcome.LOSE,
        "B X": Outcome.LOSE,
        "B Y": Outcome.DRAW,
        "B Z": Outcome.WIN,
        "C X": Outcome.WIN,
        "C Y": Outcome.LOSE,
        "C Z": Outcome.DRAW,
    }

    score = 0
    for round_ in data:
        _, play = round_.split()
        outcome = outcomes[round_]
        score += Play[play] + outcome

    return score


def part_2(data: list[str]):
    class Play(IntEnum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    class Result(IntEnum):
        X = Outcome.LOSE
        Y = Outcome.DRAW
        Z = Outcome.WIN

    strategy = {
        "A X": Play.SCISSORS,
        "A Y": Play.ROCK,
        "A Z": Play.PAPER,
        "B X": Play.ROCK,
        "B Y": Play.PAPER,
        "B Z": Play.SCISSORS,
        "C X": Play.PAPER,
        "C Y": Play.SCISSORS,
        "C Z": Play.ROCK,
    }

    score = 0
    for round_ in data:
        _, outcome = round_.split()
        play = strategy[round_]
        score += play + Result[outcome]

    return score


def main():
    with open(BASE_DIR / "d02" / "input.txt") as f:
        data = [line.strip() for line in f.readlines() if line]

    p1 = part_1(data)
    p2 = part_2(data)

    print(f"{p1=}", f"{p2=}", sep="\n")


if __name__ == "__main__":
    main()
