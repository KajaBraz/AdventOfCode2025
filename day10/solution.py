"""
Challenge Link: https://adventofcode.com/2025/day/10

Run the code to see the results of the sample input used in the description.
Paste your personal input in the dedicated file to get your result.
"""

import re
from itertools import product
from typing import List, Tuple


def solve_part_1(lights: List[List[int]], button_groups: List[List[List[int]]]) -> int:
    min_presses_sum = 0

    for i, light in enumerate(lights):
        button_group = button_groups[i]
        light_toggles_matrix = []
        # Matrix which show which button group has effect on light
        # Each row is one light element; each elem in row indicates if kth button group has effect on the light elem
        # That is, which button group can toggle on/off the light elem

        for light_i in range(len(light)):
            row = [0] * len(button_group)
            for button_i, button in enumerate(button_group):
                if light_i in button:
                    row[button_i] = 1
            light_toggles_matrix.append(row)

        min_presses = find_min_presses_light_state_change(light_toggles_matrix, light)
        min_presses_sum += min_presses

    return min_presses_sum


def press_buttons(light_toggle_matrix: List[List[int]], press_combination: Tuple[int]) -> List[int]:
    light_state = [0] * len(light_toggle_matrix)

    for i, matrix_row in enumerate(light_toggle_matrix):
        current_light_state = 0
        for j in range(len(matrix_row)):
            current_light_state = (current_light_state + (matrix_row[j] * press_combination[j])) % 2
            # current_light_state = current_light_state ^ (light_toggle_matrix[m][n] & press_combination[n])
            # If button j affects light i (row[j] == 1) and is pressed an odd number of times (press_combination[j] == 1),
            #  then the light can be toggled by the button (state change)
            #  The result of the multiplication (binary AND) is 1 only when the button affects the light and is pressed an odd number of times
            #  If the result is 1, the light state will change
        light_state[i] = current_light_state
    return light_state


def find_min_presses_light_state_change(light_toggle_matrix: List[List[int]], target_light: List[int]) -> int:
    min_presses = float('inf')

    for press_combination in product([0, 1], repeat=len(light_toggle_matrix[0])):
        if target_light == press_buttons(light_toggle_matrix, press_combination):
            min_presses = min(min_presses, sum(press_combination))

    return min_presses


def parse_input(file_path: str) -> Tuple[List[List[int]], List[List[List[int]]], List[List[int]]]:
    with open(file_path) as f:
        input_lines = [line.strip().split(' ') for line in f]
    lights, buttons, joltage = [], [], []
    for line in input_lines:
        lights.append([0 if c == '.' else 1 for c in line[0][1:-1]])
        buttons.append([[int(n) for n in re.findall(r'\d+', btns)] for btns in line[1:-1]])
        joltage.append([int(n) for n in line[-1][1:-1].split(',')])
    return lights, buttons, joltage


if __name__ == '__main__':
    sample_lights, sample_buttons, _ = parse_input('sample_input.txt')
    my_input_lights, my_input_buttons, _ = parse_input('input.txt')

    example_1 = solve_part_1(sample_lights, sample_buttons)
    part_1 = solve_part_1(my_input_lights, my_input_buttons)
    print(f'Part 1:\tExample: {example_1} | Solution: {part_1}')
