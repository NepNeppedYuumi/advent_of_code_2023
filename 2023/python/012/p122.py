from itertools import permutations, combinations, product
from datetime import datetime
from multiprocessing import Pool
from more_itertools import distinct_permutations
from math import factorial, prod


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        data = []
        for i, line in enumerate(lines):
            line, nums = line.split(' ')
            nums = [int(n) for n in nums.split(',')]
            data.append((line, nums))
    return data


def calculate_permutations_with_pattern(fixed_counts, total_elements):
    # Calculate the multinomial coefficient
    multinomial_coefficient = factorial(sum(fixed_counts)) / prod(factorial(count) for count in fixed_counts)

    # Calculate the number of variable positions
    variable_positions = total_elements - sum(fixed_counts)

    # Calculate the total permutations with the specified pattern
    total_permutations = multinomial_coefficient * factorial(variable_positions - len(fixed_counts) + 1)

    return total_permutations



def sub(vars):
    i, (line, counts) = vars
    unknown, broken = line.count('?'), line.count('#')
    total_broken = sum(counts)
    un_br, un_nbr = total_broken - broken, unknown - (total_broken - broken)
    fill_str = '#' * un_br + '.' * un_nbr
    current = calculate_permutations_with_pattern(counts, len(line))
    print(i, current)
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