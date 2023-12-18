from itertools import combinations
from functools import cache
import sys
from enum import Enum


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        lines = tuple(lines)
    return lines


def do_thing(data, start):
    points = set()
    combo = set()
    stack = [start]
    while stack:
        position, direction = stack.pop()
        x, y = position
        if x < 0 or x >= len(data) or y < 0 or y >= len(data[0]):
            continue
        if (position, direction) in combo:
            print("hi")
            continue
        points.add(position)
        combo.add((position, direction))
        char = data[x][y]

        if char == '.':
            dx, dy = direction
            stack.append(((x + dx, y + dy), direction))
        elif char == '/':
            dx, dy = tuple(-1 * n for n in direction[::-1])
            stack.append(((x + dx, y + dy), (dx, dy)))
        elif char == '\\':
            dx, dy = tuple(n for n in direction[::-1])
            stack.append(((x + dx, y + dy), (dx, dy)))
        elif char == '|':
            dx, dy = direction
            if dx == 0:
                stack.append(((x + 1, y), (1, 0)))
                stack.append(((x - 1, y), (-1, 0)))
            else:
                stack.append(((x + dx, y + dy), direction))
        elif char == '-':
            dx, dy = direction
            if dy == 0:
                stack.append(((x, y + 1), (0, 1)))
                stack.append(((x, y - 1), (0, -1)))
            else:
                stack.append(((x + dx, y + dy), direction))
    return len(points)



def pre_process(data):
    direct = {
        '/': ((0, -1), (0,))
    }



def p1(data):
    all_points = []
    for i in range(0, len(data[0])):
        all_points.append(do_thing(data, ((0, i), (1, 0))))
    for i in range(0, len(data[0])):
        all_points.append(do_thing(data, ((len(data)-1, i), (-1, 0))))
    for i in range(0, len(data)):
        all_points.append(do_thing(data, ((i, 0), (0, 1))))
    for i in range(0, len(data)):
        all_points.append(do_thing(data, ((i, len(data[0]) - 1), (0, -1))))
    highest = max(all_points)
    return highest


test_data = parser("016_test.txt")
assert p1(test_data) == 51
actual_data = parser()
print(p1(actual_data))