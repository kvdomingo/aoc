from y2025.d03.core import load_input, part1, part2


def test_part1():
    data = load_input(is_test=True)
    assert part1(data) == 357


def test_part1_alt1():
    assert part1("987654321111111") == 98


def test_part1_alt2():
    assert part1("811111111111119") == 89


def test_part1_alt3():
    assert part1("234234234234278") == 78


def test_part1_alt4():
    assert part1("818181911112111") == 92


def test_part2():
    data = load_input(is_test=True)
    assert part2(data) is None
