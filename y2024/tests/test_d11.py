from y2024.d11.core import load_input, part1


def test_part1():
    data = load_input(is_test=True)
    assert part1(data) == 55312
