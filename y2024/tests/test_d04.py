from y2024.d04.core import load_input, part1, part2


def test_part1():
    data = load_input(is_test=True)
    assert part1(data) == 18


def test_part2():
    data = load_input(is_test=True)
    assert part2(data) == 9
