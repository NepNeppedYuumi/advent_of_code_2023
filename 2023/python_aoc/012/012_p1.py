from itertools import permutations, combinations, product
from datetime import datetime


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        data = []
        for i, line in enumerate(lines):
            line, nums = line.split(' ')
            nums = [int(n) for n in nums.split(',')]
            data.append((line, nums))
    return data


def p1(data):
    total = 0
    current_time = datetime.now()
    for i, (line, counts) in enumerate(data, start=1):
        unknown, broken = line.count('?'), line.count('#')
        total_broken = sum(counts)
        un_br, un_nbr = total_broken - broken, unknown - (total_broken - broken)
        fill_str = '#' * un_br + '.' * un_nbr
        current = 0
        if i % 3 == 0:
            print(f"{i} out of 1000, {i/1000:1f}%; elapsed: {(datetime.now() - current_time)}")
        for perm in set(permutations(fill_str, len(fill_str))):
            new_str = line
            for char in perm:
                new_str = new_str.replace('?', char, 1)
            chains = [len(seq) for seq in new_str.split('.') if seq != '']
            if chains == counts:
                current += 1
        total += current
    print(total)
    return total


test_data = parser("012_test.txt")
assert p1(test_data) == 21
actual_data = parser()
print(p1(actual_data))