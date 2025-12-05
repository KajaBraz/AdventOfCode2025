"""
Challenge Link: https://adventofcode.com/2025/day/5

Run the code to see the results of the sample input used in the description.
Paste your personal input in the dedicated file to get your result.
"""

import typing


def solve_part_1(ranges: typing.List[typing.List[int]], nums: typing.List[int]) -> int:
    cnt = 0
    for n in nums:
        found = False
        i = 0
        while not found and i < len(ranges):
            a, b = ranges[i]
            if a <= n <= b:
                found = True
                cnt += 1
            i += 1
    return cnt


def solve_part_2(ranges: typing.List[typing.List[int]]) -> int:
    ranges.sort()
    merged_ranges = []
    r0 = ranges[0]

    for (a, b) in ranges[1:]:
        if a <= r0[1] + 1:
            r0[1] = max(b, r0[1])
        else:
            merged_ranges.append(r0)
            r0 = [a, b]

    merged_ranges.append(r0)
    return sum(b - a + 1 for a, b in merged_ranges)


def parse_input(file_path: str) -> typing.Tuple[typing.List[typing.List[int]], typing.List[int]]:
    with open(file_path, 'r') as f:
        content = f.read().strip()

    p1, p2 = content.split('\n\n')
    ranges = [[int(r) for r in p.split('-')] for p in p1.split()]
    nums = [int(n) for n in p2.split()]
    return ranges, nums


if __name__ == '__main__':
    sample_ranges, sample_nums = parse_input('sample_input.txt')
    my_input_ranges, my_input_nums = parse_input('input.txt')

    example_1 = solve_part_1(sample_ranges, sample_nums)
    part_1 = solve_part_1(my_input_ranges, my_input_nums)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample_ranges)
    part_2 = solve_part_2(my_input_ranges)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
