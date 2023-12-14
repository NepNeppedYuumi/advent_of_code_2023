from itertools import permutations, combinations, product
from datetime import datetime
from multiprocessing import Pool
from more_itertools import distinct_permutations
from functools import cache


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        data = []
        for i, line in enumerate(lines):
            line, nums = line.split(' ')
            nums = tuple(int(n) for n in nums.split(','))
            data.append((line, nums))
    return data


def perm(current_row, row, counts):
    if len(current_row) == 0:
        return 1


def permutationss(values, row, n=0):
    if values and values[0]:
        current, *other = values
        for i in range(len(row) - sum(other) - len(other) + 1 - current):
            if 1 not in row[i:i + current]:
                for j in permutationss(tuple(other), row[i + current + 1:], 1):
                    yield [1] * (i + n) + [2] * current + j
    else:
        yield []


def sub(vars):
    i, (line, counts) = vars
    line = '?'.join([line]*5).strip('.')
    counts = counts*5
    dic = {'?':0, '.': 1, '#':2}
    row = [dic[char] for char in line]
    unknown, broken = line.count('?'), line.count('#')
    total_broken = sum(counts)
    un_br, un_nbr = total_broken - broken, unknown - (total_broken - broken)
    fill_str = '#' * un_br + '.' * un_nbr
    current = 0
    # if line.count('.') == 0:
    #     print(f"skipping {i}")
    # else:

    for permutation in map(lambda x: x +[1] * (len(row) - len(x)), permutationss(counts, tuple(row))):

        for n1, n2 in zip(row, permutation):
            if n1 > 0 and n1 != n2:
                break
        else:
            current += 1
    print(i, current)
    return current


def p1(data):
    total = 0
    with Pool(processes=1) as pool:
        results = pool.map(sub, enumerate(data, start=1))

    total = sum(results)
    print(total)
    return total


def main():
    test_data = parser("012_test.txt")
    assert p1(test_data) == 18901
    actual_data = parser()
    print(p1(actual_data))


if __name__ == '__main__':
    main()
