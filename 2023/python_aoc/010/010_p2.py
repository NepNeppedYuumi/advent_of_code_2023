from datetime import datetime

startTime = datetime.today()


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        # data = []
        # for i, line in enumerate(lines):
        #     data.append( [int(num) for num in line.split()])
    return lines


def p1(data):
    connections = {
        "|": ((-1, 1), None),
        "-": (None, (-1, 1)),
        "L": (-1, 1),
        "J": (-1, -1),
        "7": (1, -1),
        "F": (1, 1)
    }
    not_loop = set()
    loop = False
    start = 0
    for i, string in enumerate(data):
        for j, char in enumerate(string):
            if char == 'S':
                start = (i, j)
            if start:
                break
        if start:
            break
    sx, sy = start
    frontier = [(sx -1, sy), (sx + 1, sy), (sx, sy - 1), (sx, sy + 1)]
    sets = []
    dictionary = {}

    complete = False
    for i, j in frontier:
        connect_set = {start, (i, j)}
        sets.append(connect_set)
        stack = [(i, j)]

        while True:
            current_len = len(connect_set)
            current_coords = stack.pop(-1)
            x, y = current_coords
            if data[x][y] == '.':
                connect_set.clear()
                break
            first, second = connections[data[x][y]]
            if first is None or second is None:
                if first is None and second is not None:
                    a, b = (x, y + second[0]), (x, y + second[1])
                else:
                    a, b = (x + first[0], y), (x + first[1], y)
            else:
                a, b = (x + first, y), (x, y + second)
            if a not in connect_set:
                stack.append(a)
            if b not in connect_set:
                stack.append(b)
            dictionary[current_coords] = (a, b)
            connect_set.add(a)
            connect_set.add(b)
            if len(connect_set) - current_len == 2 and current_len != 1:
                connect_set.clear()
                dictionary.clear()
                break
            if len(connect_set) - current_len == 0:
                complete = True
                break
        if complete:
            dictionary[start] = tuple(
                key for key, item in dictionary.items() if start in item)
            break

    loop = [element for element in sets if len(element) != 0][0]
    walls = set().union(loop)
    subspaces = set()
    to_escape = []
    string = ''
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            subspaces.add((i + 0.5, j + 0.5))
            if (i, j) not in loop:
                subspaces.add((i, j))
                to_escape.append((i, j))
            for d in (-1, 1):
                if (i, j) not in dictionary.get((i + d, j), ()):
                    subspaces.add((i + (d / 2), j))
                else:
                    walls.add((i + (d / 2), j))
                if (i, j) not in dictionary.get((i, j + d), ()):
                    subspaces.add((i, j + (d / 2)))
                else:
                    walls.add((i, j + (d / 2)))
    string = ''
    for i in range(len(data) * 2):
        for j in range(len(data[0]) * 2):
            if (i, j) in walls:
                string += '#'


    escaped = set()
    not_escapable = set()
    not_escaped = []
    height, width = len(data), len(data[0])
    print("time passed:", datetime.now() - startTime)
    for coord in to_escape:
        checked = {coord}
        frontier = [coord]
        while frontier:
            current = frontier.pop()
            cy, cx = current
            if (cy == -1 or cy == height
                    or cx == -1 or cx == width):
                break
            # if (current in escaped
            #         or cy == -1 or cy == height
            #         or cx == -1 or cx == width):
            #     escaped.union(checked)
            #     break
            # if current in not_escapable:
            #     not_escapable.union(checked)
            #     not_escaped.append(coord)
            #     break
            for ny in (-0.5, 0, 0.5):
                for nx in (-0.5, 0, 0.5):
                    new = (cy + ny, cx + nx)
                    if new not in checked and new not in walls:
                        frontier.append(new)
                        checked.add(new)
        else:
            # not_escapable.union(checked)
            not_escaped.append(coord)
    return len(not_escaped)


test_data = parser("010_test3.txt")
assert p1(test_data) == 4
test_data = parser("test4")
assert p1(test_data) == 4
test_data = parser("test5")
assert p1(test_data) == 10
test_data = parser("test6")
assert p1(test_data) == 8
startTime = datetime.now()
actual_data = parser()
print(p1(actual_data))
print(datetime.now() - startTime)
# test_data = parser("010_test3.txt")
# p2(test_data) == 4
# test_data = parser("test4")
# p2(test_data) == 4
# test_data = parser("test5")
# p2(test_data) == 10
# test_data = parser("test6")
# p2(test_data) == 8
