from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        lines = [list(l) for l in lines]
    return lines


def p1(data):
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col != 'O':
                continue
            rn = r
            while rn > 0 and data[rn - 1][c] == '.':
                rn -= 1
            if rn != r:
                data[rn][c] = 'O'
                data[r][c] = '.'
    print('\n'.join([''.join(r) for r in data]))
    total = 0
    count = 0
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col != 'O':
                continue
            count += 1
            total += len(data) - r
    print(total, count)
    return total


test_data = parser("014_test.txt")
assert p1(test_data) == 136
actual_data = parser()
print(p1(actual_data))