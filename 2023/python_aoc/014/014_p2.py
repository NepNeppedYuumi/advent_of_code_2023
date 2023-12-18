from itertools import combinations
from functools import cache
from datetime import datetime


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return tuple(lines)


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
    if r:
        return new_string[::-1]
    return new_string


def directions(data):
    data = zip(*map(move, zip(*data)))  # north - works
    data = map(move, data)  # west - works
    data = zip(*map(lambda x: move(x, True), zip(*data)))  # south
    return tuple(map(lambda x: move(x, True), data))  # east - works


def calc(data):
    data = tuple(data)
    total = 0
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col != 'O':
                continue
            total += len(data) - r
    return total


def p1(data):
    now = datetime.now()
    # print('\n'.join([''.join(r) for r in data]))

    cacher = {}
    cached_at = {}

    loop = 0
    while True:
        loop += 1
        if data in cacher:
            # print("cached at:", loop, "from", cached_at[data])
            data = cacher[data]
            break
        else:
            n_data = directions(data)
            cacher[data] = n_data
            cached_at[data] = loop
            data = n_data
        # print(loop, calc(data))

    loops_to_go = ((1000000000 - (cached_at[data] - 1)) %
                   ((len(cached_at) + 1) - (cached_at[data] - 1)))
    # print("loops to go", loops_to_go)
    for i in range(loops_to_go):
        data = cacher[data]
    data = tuple(data)
    total = 0
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col != 'O':
                continue
            total += len(data) - r
    print(total)
    print(datetime.now() - now)
    return total


test_data = parser("014_test.txt")
assert p1(test_data) == 64
actual_data = parser()
print(p1(actual_data))