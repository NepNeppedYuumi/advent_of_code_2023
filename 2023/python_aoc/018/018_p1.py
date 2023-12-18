from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return lines


def p1(data):
    directions = {
        'R': (0, 1),
        'L': (0, -1),
        'D': (1, 0),
        'U': (-1, 0)
    }
    points = {(0, 0)}
    x, y = (0, 0)
    for line in data:
        direction, steps, color = line.split(' ')
        dx, dy = directions[direction]
        for _ in range(int(steps)):
            x, y = x + dx, y + dy
            points.add((x, y))
    min_x = min(points, key =lambda x: x[0])[0]
    max_x = max(points, key =lambda x: x[0])[0]
    min_y = min(points, key=lambda x: x[1])[1]
    max_y = max(points, key =lambda x: x[1])[1]
    string = ''
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) in points:
                string += '#'
            else:
                string += '.'
        string += '\n'
    # print(string)
    # print(len(points))
    # print(f"it is {(3, 0) in points}")
    escaped = set()
    not_escaped = set()
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) in points:
                continue
            seen = set()
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                seen.add((cx, cy))
                if cx < min_x or cx > max_x or cy < min_y or cy > max_y or (x, y) in escaped:
                    escaped.union(seen)
                    break
                for dx, dy in directions.values():
                    new = (cx + dx, cy + dy)
                    if new in seen:
                        continue
                    if new not in points:
                        stack.append(new)
            else:
                points.add((x, y))
    string = ""
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) in points:
                string += '#'
            else:
                string += '.'
        string += '\n'
    print(string)
    print(len(points))
    print("finished")
    return len(points)


test_data = parser("018_test.txt")
assert p1(test_data) == 62
actual_data = parser()
print(p1(actual_data))
