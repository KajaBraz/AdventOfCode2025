"""
Challenge Link: https://adventofcode.com/2025/day/4

Run the code to see the results of the sample input used in the description.
Paste your personal input in the dedicated file to get your result.
"""

import typing


def solve_part_1(data: typing.List[typing.List[str]]) -> int:
    cnt = 0
    for i, row in enumerate(data):
        for j in range(len(row)):
            if data[i][j] == '@':
                neighs_cnt = len(get_neighbouring_rolls(data, i, j))
                cnt += 1 if neighs_cnt < 4 else 0
    return cnt


def solve_part_2(data: typing.List[typing.List[str]]) -> int:
    to_remove = [(-1, -1)]
    removed = 0
    while to_remove:
        to_remove = get_rolls_to_remove(data)
        removed += len(to_remove)
        remove_rolls(data, to_remove)
    return removed


def get_neighbouring_rolls(data: typing.List[typing.List[str]], i: int, j: int) -> typing.List[typing.Tuple[int, int]]:
    dirs = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
    neighs = [(ni + i, nj + j) for ni, nj in dirs if
              0 <= ni + i < len(data) and 0 <= nj + j < len(data[0]) and data[ni + i][nj + j] == '@']
    return neighs


def get_rolls_to_remove(data: typing.List[typing.List[str]]) -> typing.List[typing.Tuple[int, int]]:
    to_remove = []
    for i, row in enumerate(data):
        for j in range(len(row)):
            if data[i][j] == '@' and len(get_neighbouring_rolls(data, i, j)) < 4:
                to_remove.append((i, j))
    return to_remove


def remove_rolls(data: typing.List[typing.List[str]], to_remove: typing.List[typing.Tuple[int, int]]) -> None:
    for i, j in to_remove:
        data[i][j] = '.'


def parse_input(file_path: str) -> typing.List[typing.List[str]]:
    with open(file_path) as f:
        input_lines = [[c for c in line.strip()] for line in f]
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
