from d02.core import load_input, part1, part2


def test_part1():
    data = load_input(is_test=True)
    assert part1(data) == 2


def test_part2():
    data = load_input(is_test=True)
    assert part2(data) == 4
