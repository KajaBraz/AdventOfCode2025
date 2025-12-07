"""
Challenge Link: https://adventofcode.com/2025/day/7

Run the code to see the results of the sample input used in the description.
Paste your personal input in the dedicated file to get your result.
"""

import typing
from collections import defaultdict


def solve_part_1(data: typing.List[str]) -> int:
    si, sj = get_start(data)
    beams = {sj}
    split_cnt = 0

    for i, row in enumerate(data[si:], start=si):
        next_row_beams = set()
        while beams:
            bj = beams.pop()
            if 0 <= bj < len(row):
                if row[bj] == '^':
                    split_cnt += 1
                    next_row_beams.add(bj - 1)
                    next_row_beams.add(bj + 1)
                else:
                    next_row_beams.add(bj)

        beams = next_row_beams
    return split_cnt


def solve_part_2(data: typing.List[str]) -> int:
    si, sj = get_start(data)
    current_paths = defaultdict(int)  # col: paths_cnt
    current_paths[sj] = 1
    completed_paths_cnt = 0

    for i, row in enumerate(data[si:], start=si):
        next_paths = defaultdict(int)

        while current_paths:
            col, cnt = current_paths.popitem()
            if row[col] != '^':
                next_paths[col] += cnt
            else:
                if 0 <= col - 1 < len(row):
                    next_paths[col - 1] += cnt
                else:
                    completed_paths_cnt += cnt

                if 0 <= col + 1 < len(row):
                    next_paths[col + 1] += cnt
                else:
                    completed_paths_cnt += cnt

        current_paths = next_paths

    completed_paths_cnt += sum(current_paths.values())
    return completed_paths_cnt


def get_start(data: typing.List[str]) -> typing.Tuple[int | None, int | None]:
    for i, row in enumerate(data):
        if 'S' in row:
            return i, row.index('S')
    return None, None


def parse_input(file_path: str) -> typing.List[str]:
    with open(file_path) as f:
        input_lines = [line.strip() for line in f]
    return input_lines


if __name__ == '__main__':
    sample = parse_input('sample_input.txt')
    my_input = parse_input('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
