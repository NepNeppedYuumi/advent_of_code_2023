from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return lines


def p1(data):
    a, b = [], []
    for line in data:
        aa, bb = line.split()
        a.append(int(aa))
        b.append(int(bb))
    a.sort()
    b.sort()
    total = 0
    for aa, bb in zip(a, b):
        total += abs(aa - bb)
    return total


def p2(data):
    a, b = [], []
    for line in data:
        aa, bb = line.split()
        a.append(int(aa))
        b.append(int(bb))
    right = {}
    for bb in b:
        times = right.get(bb, 0)
        right[bb] = times + 1
    total = 0
    for aa in a:
        total += right.get(aa, 0) * aa
    return total



test_data = parser("001_test.txt")
assert p1(test_data) == 11
actual_data = parser()
print(p1(actual_data))

test_data = parser("001_test.txt")
assert p2(test_data) == 31
actual_data = parser()
print(p2(actual_data))


test_data = parser("001_test.txt")
assert p2_want_marc_cringe(test_data) == 31
actual_data = parser()
print(p2_want_marc_cringe(actual_data))