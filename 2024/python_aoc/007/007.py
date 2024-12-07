from itertools import combinations
from collections import defaultdict
from time import time


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return lines


def p1(data):
    total = 0
    for line in data:
        needed, nums = line.split(": ")
        needed = int(needed)
        nums = [int(n) for n in nums.split(" ")]
        between = [nums[0]]
        new_between = []
        for n in nums[1:]:
            for b in between:
                new_between.append(b * n)
                new_between.append(b + n)
            between = new_between.copy()
            new_between.clear()
        
        if needed in between:
            total += needed
    print(total)
    return total


def p2(data):
    total = 0
    for line in data:
        needed, nums = line.split(": ")
        needed = int(needed)
        nums = [int(n) for n in nums.split(" ")]
        between = [nums[0]]
        new_between = []
        for n in nums[1:]:
            for b in between:
                new_between.append(b * n)
                new_between.append(b + n)
                new_between.append(int(str(b) + str(n)))
            between = new_between.copy()
            new_between.clear()
        
        if needed in between:
            total += needed
    return total



test_data = parser("007_test")
assert p1(test_data) == 3749
actual_data = parser()
print(p1(actual_data))

start = time()
test_data = parser("007_test")
assert p2(test_data) == 11387
actual_data = parser()
print(p2(actual_data))
print("time:", time() - start)

