from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return lines


def move(string, r=False):
    empty_count = 0
    new_string = ""
    if r:
        loop = range(len(string)-1, -1, -1)
    else:
        loop = range(0, len(string))
    for i in loop:
        if string[i] == 'O':
            new_string += 'O'
        elif string[i] == '#':
            new_string += "." * empty_count + '#'
            empty_count = 0
        else:
            empty_count += 1
    new_string += "." * empty_count
    return new_string


def directions(data):
    data = map(move, data)  # west
    data = map(lambda x: move(x, True), data)  # east
    data = zip(*map(move, zip(*data)))  # north
    data = zip(*map(lambda x: move(x, True), zip(*data)))  # south


def p1(data):
    # print('\n'.join([''.join(r) for r in data]))
    print()
    data = zip(*map(move, zip(*data)))  # north
    # print('\n'.join([''.join(r) for r in data]))
    total = 0
    print("what")
    print(data)
    data = tuple(data)
    for r, row in enumerate(data):
        print(row)
        for c, col in enumerate(row):
            if col != 'O':
                continue
            total += len(data) - r
    print(total)
    return total


test_data = parser("014_test.txt")
assert p1(test_data) == 136
actual_data = parser()
print(p1(actual_data))