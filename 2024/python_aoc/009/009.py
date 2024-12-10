from collections import defaultdict
from itertools import combinations, permutations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().strip()
    return lines


def p1(data):
    total = 0
    position = 0
    left = 0
    right = len(data) - 1
    part_right = 0
    while left < right:
        subtotal = 0
        for i in range(position, position + int(data[left])):
            
            subtotal += i * (left >> 1)
            position += 1
        total += subtotal
        empty = int(data[left + 1])
        for i in range(empty):
            total += position * ((right >> 1))
            part_right += 1
            position += 1
            if part_right >= int(data[right]):
                right -= 2
                part_right = 0
        left += 2
    for i in range(position, position + (int(data[left]) - part_right)):
        total += i * (left >> 1)
    return total


def p2(data):
    print(data)
    total = 0
    position = 0
    left = 0
    right = len(data) - 1
    part_right = 0
    moved_into = {}
    
    position_at_empy = {}
    mark = 0
    for i, c in enumerate(data):
        if i % 2 != 0:
            position_at_empy[i] = mark
        mark += int(data[i])
    
    while right > 1:
        subtotal = 0
        if left <= right:
            for i in range(position, position + int(data[left])):
                subtotal += i * (left >> 1)
                position += 1
        position += int(data[left + 1])
        total += subtotal
        right_num = int(data[right])
        for i in range(1, right, 2):
            og_empty = int(data[i])
            empty = og_empty - moved_into.get(i, 0)

            if empty >= right_num:
                new_pos = position_at_empy[i] + moved_into.get(i, 0)
                moved_into[i] = moved_into.get(i, 0) + right_num
                break
        else:
            new_pos = position_at_empy[right - 1] + int(data[right - 1])
        for pos in range(new_pos, new_pos + right_num):
            total += pos * (right >> 1)
        if left > right:
            new_pos = position_at_empy[right - 1] + int(data[right - 1])
            for pos in range(new_pos, new_pos + right_num):
                total -= pos * (right >> 1)
        right -= 2
        left += 2

    print(total)
    return total
    


# test_data = parser("009_test.txt")
# assert p1(test_data) == 1928
# actual_data = parser()
# print(p1(actual_data))

test_data = parser("009_test.txt")
assert p2(test_data) == 2858
actual_data = parser()
print(p2(actual_data))


