from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return lines


def p1():
    return None


test_data = parser("011_test.txt")
assert p1(test_data) == 374
actual_data = parser()
print(p1(actual_data))