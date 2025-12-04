"""
Challenge Link: https://adventofcode.com/2025/day/3

Run the code to see the results of the sample input used in the description.
Paste your personal input in the dedicated file to get your result.
"""

import typing


def solve_part_1(data: typing.List[str]) -> int:
    return sum(get_largest(row, 2) for row in data)


def solve_part_2(data: typing.List[str]) -> int:
    return sum(get_largest(row, 12) for row in data)


def get_largest(row: str, needed_digits: int) -> int:
    largest = []
    cur_i = 0

    while needed_digits > 0:
        available_digits = len(row) - cur_i
        extra_digits_cnt = available_digits - needed_digits
        end_i = cur_i + extra_digits_cnt + 1
        window = row[cur_i:end_i]
        t = (0, '0')

        for j, d in enumerate(window):
            t = max([t, (j, d)], key=lambda x: x[1])

        max_d_i, max_d = t
        largest.append(max_d)
        cur_i += (max_d_i + 1)
        needed_digits -= 1
    return int(''.join(largest))


def parse_input(file_path: str) -> typing.List[str]:
    with open(file_path) as f:
        input_lines = [line.strip() for line in f]
    return input_lines


def solve_part_1_brute_force(data: typing.List[str]) -> int:
    nums = []
    for row in data:
        row = [int(d) for d in row]
        num = 0
        for i, n in enumerate(row[:-1]):
            for m in row[i + 1:]:
                num = max(n * 10 + m, num)
        nums.append(num)
    return sum(nums)


if __name__ == '__main__':
    sample = parse_input('sample_input.txt')
    my_input = parse_input('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')

