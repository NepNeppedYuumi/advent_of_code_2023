from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return lines


def p2(data, increase=1000000):
    fake_coords = []
    xs, ys = set(), set()
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "#":
                fake_coords.append((i, j))
    xs = {i for i in range(len(data)) if i not in {x for x, _ in fake_coords}}
    ys = {i for i in range(len(data[0])) if i not in {y for _, y in fake_coords}}
    coords = []
    x = 0
    for i, line in enumerate(data):
        if i in xs:
            x += (1 * increase) - 1
            continue
        y = 0
        for j, char in enumerate(line):
            if j in ys:
                y += (1 * increase) - 1
                continue
            if char == '#':
                coords.append((i + x, j + y))
    combi = list(combinations(coords, r=2))
    total = 0
    for i, ((ax, ay), (bx, by)) in enumerate(combi):
        # if not ( (ax, ay) == (6, 1) and (11, 5) == (bx, by)):
        #     continue
        diffx, diffy = ax - bx, ay - by
        total += abs(diffx) + abs(diffy)
    print(total)
    return total


test_data = parser("011_test.txt")
assert p2(test_data, 2) == 374
assert p2(test_data, 10) == 1030
assert p2(test_data, 100) == 8410
actual_data = parser()
print(p2(actual_data))