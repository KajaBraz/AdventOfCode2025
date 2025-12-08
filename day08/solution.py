"""
Challenge Link: https://adventofcode.com/2025/day/8

Run the code to see the results of the sample input used in the description.
Paste your personal input in the dedicated file to get your result.
"""

import math
import operator
import typing
from collections import defaultdict, deque
from functools import reduce


def solve_part_1(data: typing.List[typing.Tuple[int]], n: int) -> int:
    distances = sorted(find_distances(data).items(), key=lambda item: item[1])
    circuits_graph = defaultdict(list)
    seen = set()
    sizes = []

    for (b1, b2), dist in distances[:n]:
        circuits_graph[b1].append(b2)
        circuits_graph[b2].append(b1)

    for p in data:
        if p not in seen:
            sizes.append(get_size_dfs(circuits_graph, p, seen))

    sizes = sorted(sizes, reverse=True)
    return reduce(operator.mul, sizes[:3])


def solve_part_2(data: typing.List[typing.Tuple[int]]) -> int:
    distances = sorted(find_distances(data).items(), key=lambda item: item[1])
    circuits = defaultdict(list)
    connections_cnt = 0

    for (b1, b2), _ in distances:
        if not path_exists_bfs(circuits, b1, b2):
            connections_cnt += 1
            circuits[b1].append(b2)
            circuits[b2].append(b1)
        if connections_cnt == len(data) - 1:
            return b1[0] * b2[0]
    return -1


def get_size_dfs(graph: typing.Dict[typing.Tuple[int], typing.List[typing.Tuple[int]]], start_node: typing.Tuple[int],
                 seen: typing.Set[typing.Tuple[int]]) -> int:
    stack = [start_node]
    size = 0
    while stack:
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            size += 1
            for neigh in graph[node]:
                stack.append(neigh)
    return size


def path_exists_bfs(graph: typing.Dict[typing.Tuple[int], typing.List[typing.Tuple[int]]],
                    start_node: typing.Tuple[int], target_node: typing.Tuple[int]) -> bool:
    queue = deque([start_node])
    seen = {start_node}

    while queue:
        node = queue.popleft()
        if node == target_node:
            return True
        for neigh in graph[node]:
            if neigh not in seen:
                seen.add(neigh)
                queue.append(neigh)
    return False


def find_distances(data: typing.List[typing.Tuple[int]]) -> \
        typing.Dict[typing.Tuple[typing.Tuple[int], typing.Tuple[int]], float]:
    d = {}
    for i, p1 in enumerate(data):
        for p2 in data[i + 1:]:
            d[(p1, p2)] = math.dist(p1, p2)
    return d


def parse_input(file_path: str) -> typing.List[typing.Tuple[int]]:
    with open(file_path) as f:
        input_lines = [line.strip().split(',') for line in f]
    return [tuple(int(n) for n in row) for row in input_lines]


if __name__ == '__main__':
    sample = parse_input('sample_input.txt')
    my_input = parse_input('input.txt')

    example_1 = solve_part_1(sample, 10)
    part_1 = solve_part_1(my_input, 1000)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    example_2 = solve_part_2(sample)
    part_2 = solve_part_2(my_input)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
