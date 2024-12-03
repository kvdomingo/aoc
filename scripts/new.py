import os
import shutil
from argparse import ArgumentParser

from jinja2 import Environment, FileSystemLoader, select_autoescape

from common.config import BASE_DIR

FILES_TO_COPY = ["__init__.py", "__main__.py"]


def main(year: int, day: int, solution1: int, solution2: int):
    env = Environment(
        loader=FileSystemLoader(BASE_DIR / "template"),
        autoescape=select_autoescape(),
    )
    core_template = env.get_template("core.py.j2")
    test_template = env.get_template("test.py.j2")

    os.makedirs(BASE_DIR / f"y{year}/d{day:02}", exist_ok=True)
    os.makedirs(BASE_DIR / f"y{year}/tests", exist_ok=True)

    for file in FILES_TO_COPY:
        shutil.copy(
            BASE_DIR / "template" / file, BASE_DIR / f"y{year}/d{day:02}" / file
        )

    with open(BASE_DIR / f"y{year}/d{day:02}/core.py", "w") as f:
        f.write(core_template.render(year=year, day=day))

    with open(BASE_DIR / f"y{year}/tests/test_d{day:02}.py", "w") as f:
        f.write(
            test_template.render(
                year=year,
                day=day,
                part1_solution=solution1,
                part2_solution=solution2,
            )
        )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-y", "--year", help="Advent of Code year", type=int)
    parser.add_argument("-d", "--day", help="Advent of Code day", type=int)
    parser.add_argument("-s1", "--solution1", help="Part 1 test solution", type=int)
    parser.add_argument("-s2", "--solution2", help="Part 2 test solution", type=int)
    args = parser.parse_args()

    main(
        year=args.year,
        day=args.day,
        solution1=args.solution1,
        solution2=args.solution2,
    )
