from y2025.d06.core import load_input, part1, part2


def test_part1():
    data = load_input(is_test=True, strip_extra_whitespace=False)
    assert part1(data) == 4277556


def test_part2():
    data = load_input(is_test=True, strip_extra_whitespace=False)
    assert part2(data) == 3263827
