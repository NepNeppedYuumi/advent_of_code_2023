from itertools import combinations
from functools import cache
import sys


sys.setrecursionlimit(1000000)


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        lines = tuple(lines)
    return lines


@cache
def move(position: tuple[int, int], direction: tuple[int, int]):
    x, y = position
    char = data[x][y]
    if char == '.':
        dx, dy = direction
        return move((x + dx, y + dy), direction)
    elif char == '/':
        dx, dy = tuple(-1 * n for n in direction[::-1])
        return move((x + dx, y + dy), (dx, dy))
    elif char == '\\':
        dx, dy = tuple(n for n in direction[::-1])
        return move((x + dx, y + dy), (dx, dy))
    elif char == '|':
        dx, dy = direction
        if dx == 0:
            return move((x + 1, y), (1, 0)), move((x - 1, y), (-1, 0))
        return move((x + dx, y + dy), direction)
    elif char == '-':
        dx, dy = direction
        if dy == 0:
            return move((x, y + 1), (0, 1)), move((x, y - 1), (0, -1))
        return move((x + dx, y + dy), direction)
    print("hi?")
    raise BrokenPipeError


def p1(data):
    points = set()
    combo = set()
    stack = [((0, 0), (0, 1))]
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
    print(len(points))
    return len(points)


test_data = parser("016_test.txt")
assert p1(test_data) == 46
actual_data = parser()
print(p1(actual_data))