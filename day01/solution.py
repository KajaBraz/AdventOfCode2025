"""
Challenge Link: https://adventofcode.com/2025/day/1

Run the code to see the results of the sample input used in the description.
Paste your personal input in the dedicated file to get your result.
"""

import typing


def solve_part_1(data: typing.List[typing.Tuple[str, int]]):
    position = 50
    cnt = 0
    for d, v in data:
        sign = -1 if d == 'L' else 1
        position += (v * sign)
        position = position % 100
        if position == 0:
            cnt += 1
    return cnt


def solve_part_2(data: typing.List[typing.Tuple[str, int]]) -> int:
    position = 50
    cnt = 0
    for d, v in data:
        sign = -1 if d == 'L' else 1
        cnt += count_intermediate_zeros(position, v, sign == 1)
        position += (v * sign)
        position = position % 100
    return cnt


def count_intermediate_zeros(position: int, steps: int, is_right: bool) -> int:
    initial_zero = 0 if position != 0 else 1
    if is_right:
        return (position + steps) // 100
    return max((steps - position) // 100 + 1 - initial_zero, 0)


def parse_input(file_path: str) -> typing.List[typing.Tuple[str, int]]:
    with open(file_path) as f:
        input_lines = [(line[0], int(line[1:])) for line in f]
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
