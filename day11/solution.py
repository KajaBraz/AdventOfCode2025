"""
Challenge Link: https://adventofcode.com/2025/day/11

Run the code to see the results of the sample input used in the description.
Paste your personal input in the dedicated file to get your result.
"""

import collections
import typing
from collections import defaultdict


def solve_part_1(data: collections.defaultdict[str, typing.List[str]]) -> int:
    start, end = 'you', 'out'
    memo = {}
    return count_paths(start, end, data, memo)


def solve_part_2(data: collections.defaultdict[str, typing.List[str]]) -> int:
    start, end = 'svr', 'out'
    required_1, required_2 = 'dac', 'fft'
    memo = {}

    cnt_start_required_1 = count_paths(start, required_1, data, memo)
    cnt_required_1_required_2 = count_paths(required_1, required_2, data, memo)
    cnt_required_2_end = count_paths(required_2, end, data, memo)

    cnt_start_required_2 = count_paths(start, required_2, data, memo)
    cnt_required_2_required_1 = count_paths(required_2, required_1, data, memo)
    cnt_required_1_end = count_paths(required_1, end, data, memo)

    path_cnt_1 = cnt_start_required_1 * cnt_required_1_required_2 * cnt_required_2_end
    path_cnt_2 = cnt_start_required_2 * cnt_required_2_required_1 * cnt_required_1_end
    return path_cnt_1 + path_cnt_2


def count_paths(start_node: str, end_node: str, graph: collections.defaultdict[str, typing.List[str]],
                memo: typing.Dict[typing.Tuple[str, str], int]):
    if (start_node, end_node) in memo:
        return memo[(start_node, end_node)]
    if start_node == end_node:
        return 1
    if start_node not in graph:
        return 0
    paths_cnt = 0
    for next_node in graph[start_node]:
        paths_cnt += count_paths(next_node, end_node, graph, memo)
    memo[(start_node, end_node)] = paths_cnt
    return paths_cnt


def parse_input(file_path: str) -> collections.defaultdict[str, typing.List[str]]:
    graph = defaultdict(list)
    with open(file_path) as f:
        input_lines = [line.strip().split(': ') for line in f]
    for line in input_lines:
        device = line[0]
        outputs = line[1].split()
        graph[device].extend(outputs)
    return graph


if __name__ == '__main__':
    sample_1 = parse_input('sample_input_1.txt')
    sample_2 = parse_input('sample_input_2.txt')
    my_input = parse_input('input.txt')

    example_1 = solve_part_1(sample_1)
    part_1 = solve_part_1(my_input)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample_2)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
