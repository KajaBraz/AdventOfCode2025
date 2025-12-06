"""
Challenge Link: https://adventofcode.com/2025/day/6

Run the code to see the results of the sample input used in the description.
Paste your personal input in the dedicated file to get your result.
"""

import typing


def solve_part_1(data: typing.List[typing.List[str]]) -> int:
    total, temp = 0, 0
    for i in range(len(data[0])):
        if data[-1][i] == '+':
            temp = sum(int(row[i]) for row in data[:-1])
        elif data[-1][i] == '*':
            temp = 1
            for row in data[:-1]:
                temp *= int(row[i])
        else:
            print('Warning: unhandled sign')
        total += temp
    return total


def solve_part_2(data: typing.List[typing.List[int | str]]) -> int:
    total, temp = 0, 0
    for row in data:
        if row[0] == '+':
            temp = sum(n for n in row[1:])
        elif row[0] == '*':
            temp = 1
            for n in row[1:]:
                temp *= n
        else:
            print('Warning: unhandled sign')
        total += temp
    return total


def parse_input_1(file_path: str) -> typing.List[typing.List[str]]:
    with open(file_path) as f:
        input_lines = [line.strip().split() for line in f]
    return input_lines


def parse_input_2(file_path: str) -> typing.List[typing.List[int | str]]:
    with open(file_path) as f:
        input_lines = [line for line in f]

    transposed = (''.join(row[i] for row in input_lines) for i in range(len(input_lines[0]) - 1))
    transposed_grouped = [[]]
    for x in transposed:
        x = x.strip()
        if x == '':
            transposed_grouped.append([])
        else:
            transposed_grouped[-1].append(x)

    normalised = []
    for i, row in enumerate(transposed_grouped):
        normalised.append([row[0][-1]])
        transposed_grouped[i][0] = transposed_grouped[i][0][:-1].strip()
        for n in transposed_grouped[i]:
            normalised[-1].append(int(n))
    return normalised


if __name__ == '__main__':
    sample_1 = parse_input_1('sample_input.txt')
    my_input_1 = parse_input_1('input.txt')

    example_1 = solve_part_1(sample_1)
    part_1 = solve_part_1(my_input_1)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')

    sample_2 = parse_input_2('sample_input.txt')
    my_input_2 = parse_input_2('input.txt')

    example_2 = solve_part_2(sample_2)
    part_2 = solve_part_2(my_input_2)
    print(f'Part 2:\tExample: {example_2} | Solution: {part_2}')
