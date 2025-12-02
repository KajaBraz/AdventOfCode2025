"""
Challenge Link: https://adventofcode.com/2025/day/2

Run the code to see the results of the sample input used in the description.
Paste your personal input in the dedicated file to get your result.
"""

import typing


def solve_part_1(data: typing.List[typing.List[int]]) -> int:
    return sum(sum_repeated_twice(n, m) for n, m in data)


def solve_part_2(data: typing.List[typing.List[int]]) -> int:
    return sum(sum_repeated_multiple(n, m) for n, m in data)


def sum_repeated_twice(start: int, end: int) -> int:
    return sum(n for n in range(start, end + 1) if is_repeated_twice(n))


def sum_repeated_multiple(start: int, end: int) -> int:
    return sum(n for n in range(start, end + 1) if is_repeated_multiple(n))


def is_repeated_twice(n: int) -> bool:
    s_num = str(n)
    length = len(s_num)

    if length % 2 == 0:
        mid = length // 2
        first_half = s_num[:mid]
        second_half = s_num[mid:]
        return first_half == second_half
    return False


def is_repeated_multiple(n: int) -> bool:
    s_num = str(n)
    length = len(s_num)

    for k in range(1, length // 2 + 1):
        if length % k == 0:
            repeat_times = length // k
            pattern = s_num[:k]
            if pattern * repeat_times == s_num:
                return True
    return False


def parse_input(file_path: str) -> typing.List[typing.List[int]]:
    with open(file_path) as f:
        ranges = (r.split('-') for r in f.read().rstrip().split(',') if r)
    return [[int(n) for n in r] for r in ranges]


if __name__ == '__main__':
    sample = parse_input('sample_input.txt')
    my_input = parse_input('input.txt')

    example_1 = solve_part_1(sample)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
