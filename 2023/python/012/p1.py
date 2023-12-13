from itertools import permutations, combinations, product
from datetime import datetime
from multiprocessing import Pool
from functools import partial


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        data = []
        for i, line in enumerate(lines):
            line, nums = line.split(' ')
            nums = [int(n) for n in nums.split(',')]
            data.append((line, nums))
    return data


def process_permutation(perm, line, counts):
    new_str = line
    for char in perm:
        new_str = new_str.replace('?', char, 1)
    chains = [len(seq) for seq in new_str.split('.') if seq != '']
    return chains == counts


def process_perm_wrapper(perm, line, counts):
    return process_permutation(perm, line, counts)


def p1(data):
    total = 0
    current_time = datetime.now()
    num_processes = 50
    for i, (line, counts) in enumerate(data, start=1):

        unknown, broken = line.count('?'), line.count('#')
        total_broken = sum(counts)
        un_br, un_nbr = total_broken - broken, unknown - (total_broken - broken)
        fill_str = '#' * un_br + '.' * un_nbr
        if i % 3 == 0:
            print(f"{i} out of 1000, {i/1000:1f}%; elapsed: {(datetime.now() - current_time)}")
        permutations_set = set(permutations(fill_str, len(fill_str)))



        proc = partial(process_perm_wrapper, line=line, counts=counts)

        with Pool(num_processes) as pool:
            results = pool.map(proc, permutations_set)

        current = sum(results)

        total += current
    print(total)
    return total


def main():
    test_data = parser("012_test.txt")
    assert p1(test_data) == 21
    actual_data = parser()
    print(p1(actual_data))


if __name__ == '__main__':
    main()