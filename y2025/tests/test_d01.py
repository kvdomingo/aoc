from y2025.d01.core import load_input, part1, part2


def test_part1():
    data = load_input(is_test=True)
    assert part1(data) == 3


def test_part2():
    data = load_input(is_test=True)
    assert part2(data) == 6


def test_part2_alt1():
    data = "\n".join(["L50", "R101"])
    assert part2(data) == 2
