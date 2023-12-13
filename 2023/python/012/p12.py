from itertools import permutations, combinations, product
from datetime import datetime
from multiprocessing import Pool
from more_itertools import distinct_permutations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        data = []
        for i, line in enumerate(lines):
            line, nums = line.split(' ')
            nums = [int(n) for n in nums.split(',')]
            data.append((line, nums))
    return data


def sub(vars):
    i, (line, counts) = vars
    unknown, broken = line.count('?'), line.count('#')
    total_broken = sum(counts)
    un_br, un_nbr = total_broken - broken, unknown - (total_broken - broken)
    fill_str = '#' * un_br + '.' * un_nbr
    current = 0
    fill_perms = distinct_permutations(fill_str, len(fill_str))
    for perm in fill_perms:
        new_str = list(line)
        char_index = 0
        for j in range(len(new_str)):
            if new_str[j] == '?':
                new_str[j] = perm[char_index]
                char_index += 1
        chains = [len(seq) for seq in ''.join(new_str).split('.') if seq != '']
        if chains == counts:
            current += 1
    print(i)
    return current


def p1(data):
    total = 0
    with Pool(processes=50) as pool:
        results = pool.map(sub, enumerate(data, start=1))

    total = sum(results)
    print(total)
    return total


def main():
    test_data = parser("012_test.txt")
    assert p1(test_data) == 21
    actual_data = parser()
    print(p1(actual_data))


if __name__ == '__main__':
    main()