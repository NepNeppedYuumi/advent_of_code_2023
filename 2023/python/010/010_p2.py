

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
    frontier = [(sx -1, sy), (sx + 1, sy), (sx, sy -1), (sx, sy +1)]
    sets = []
    # print(start)
    # print(frontier)
    for i, j in frontier:
        connect_set = {start, (i, j)}
        sets.append(connect_set)
        stack = [(i, j)]
        # print((i, j))
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
                    a, b = (x, y+second[0]), (x, y+second[1])
                else:
                    a, b = (x + first[0], y), (x + first[1], y)
            else:
                a, b = (x+first, y), (x, y+second)
            if a not in connect_set:
                stack.append(a)
            if b not in connect_set:
                stack.append(b)
            connect_set.add(a)
            connect_set.add(b)
            if len(connect_set) - current_len == 2 and current_len != 1:
                # print("hi")
                # print(connect_set, len(connect_set))
                # print(current_coords, a, b)
                connect_set.clear()
                break
            if len(connect_set) - current_len == 0:
                break
        # print(connect_set)
        # print(len(connect_set))
    # print(sets)
    loop = [element for element in sets if len(element) != 0][0]
    escape_set = set()
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char != '.':
                continue
    return distance


test_data = parser("010_test3.txt")
assert p1(test_data) == 4
test_data = parser("test4")
assert p1(test_data) == 4
test_data = parser("test5")
assert p1(test_data) == 8
actual_data = parser()
print(p1(actual_data))