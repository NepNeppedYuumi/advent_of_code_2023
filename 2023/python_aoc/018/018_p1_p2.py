from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return lines

import numpy as np
def pathArea(path):
    # Less than three points, and the area is zero.
    if len(path) < 3:
        return 0

    A = 0.0
    for i in range(0, len(path)):
        A += path[i-1][0] * path[i][1] - path[i][0] * path[i-1][1]

    return 0.5 * abs(A)


def polygon_area(points):
    """Return the area of the polygon whose vertices are given by the
    sequence points.

    """
    area = 0
    q = points[-1]
    for p in points:
        area += p[0] * q[1] - p[1] * q[0]
        q = p
    return area / 2


def p1(data):
    directions = {
        'R': (0, 1),
        'L': (0, -1),
        'D': (1, 0),
        'U': (-1, 0)
    }
    points = []
    total_points = 0
    x, y = (0, 0)
    for line in data:
        direction, steps, color = line.split(' ')
        steps = int(steps)
        dx, dy = directions[direction]
        x, y = x + steps * dx, y + steps * dy
        total_points += steps
        points.append((x, y))
    area = pathArea(points)
    area = area + (total_points / 2) + 1
    print(area)
    return area


test_data = parser("018_test.txt")
assert p1(test_data) == 62
actual_data = parser()
print(p1(actual_data))
