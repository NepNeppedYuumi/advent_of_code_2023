from collections import defaultdict
from itertools import combinations, permutations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = [list(x) for x in file.read().splitlines()]
    return lines


def p1(data):
    antennas = defaultdict(lambda: [])
    for x, line in enumerate(data):
        for y, c in enumerate(line):
            if c == ".":
                continue
            antennas[c].append((x, y))
    anti = set()
    for key, value in antennas.items():
        if len(value) < 2:
            print("not enough to do")
            pass
        for a, b in combinations(value, 2):
            (ax, ay), (bx, by) = a, b
            
            dx, dy = bx - ax, by - ay
            new1 = (ax - dx, ay - dy)
            new2 = (bx + dx, by + dy)
            for nx, ny in [new1, new2]:
                if nx < 0 or nx >= len(data) or ny < 0 or ny >= len(data[0]):
                    continue
                anti.add((nx, ny))
    total = len(anti)
    # print(total)
    # for x, y in anti:
    #     data[x][y] = "#"
    #
    # for x, line in enumerate(data):
    #     for y, c in enumerate(line):
    #         print(c, end="")
    #     print("\n", end='')
    return total


def p2(data):
    antennas = defaultdict(lambda: [])
    for x, line in enumerate(data):
        for y, c in enumerate(line):
            if c == ".":
                continue
            antennas[c].append((x, y))
    anti = set()
    for key, value in antennas.items():
        if len(value) < 2:
            print("not enough to do")
            pass
        for a, b in combinations(value, 2):
            (ax, ay), (bx, by) = a, b
            anti.add(a)
            anti.add(b)
            
            dx, dy = bx - ax, by - ay
            old = (ax, ay)
            while True:
                ox, oy = old
                nx, ny = (ox - dx, oy - dy)
                if nx < 0 or nx >= len(data) or ny < 0 or ny >= len(data[0]):
                    break
                anti.add((nx, ny))
                old = (nx, ny)
            
            old = (bx, by)
            while True:
                ox, oy = old
                nx, ny = (ox + dx, oy + dy)
                if nx < 0 or nx >= len(data) or ny < 0 or ny >= len(data[0]):
                    break
                anti.add((nx, ny))
                old = (nx, ny)

                
    total = len(anti)
    print(total)
    # for x, y in anti:
    #     data[x][y] = "#"
    #
    # for x, line in enumerate(data):
    #     for y, c in enumerate(line):
    #         print(c, end="")
    #     print("\n", end='')
    return total


test_data = parser("008_test.txt")
assert p1(test_data) == 14
actual_data = parser()
print(p1(actual_data))


test_data = parser("008_test.txt")
assert p2(test_data) == 34
actual_data = parser()
print(p2(actual_data))


