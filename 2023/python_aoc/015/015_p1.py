from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().strip().split(',')
    return lines


def p1(data):
    total = 0
    for word in data:
        num = 0
        for c in word:
            num += ord(c)
            num *= 17
            num = num % 256
        total += num
        print(num)
    print(total)
    return total


test_data = parser("015_test.txt")
assert p1(test_data) == 1320
actual_data = parser()
print(p1(actual_data))