from collections import defaultdict
from itertools import combinations, permutations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().strip().split()
    return lines


def p1(data):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    total = 0
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char != "0":
                continue
            nines = set()
            to_visit = [(r, c)]
            while len(to_visit):
                cr, cc = to_visit.pop()
                if data[cr][cc] == "9":
                    nines.add((cr, cc))
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if nr < 0 or nr >= len(data) or nc < 0 or nc >= len(data[0]):
                        continue
                    if ord(data[cr][cc]) + 1 == ord(data[nr][nc]):
                        to_visit.append((nr, nc))
            total += len(nines)
    print(total)
    return total


def p2(data):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    total = 0
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char != "0":
                continue
            nines = set()
            to_visit = [[(r, c)]]
            while len(to_visit):
                current = to_visit.pop()
                cr, cc = current[-1]
                if data[cr][cc] == "9":
                    nines.add(tuple(current))
                    continue
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if nr < 0 or nr >= len(data) or nc < 0 or nc >= len(data[0]):
                        continue
                    if ord(data[cr][cc]) + 1 == ord(data[nr][nc]):
                        to_visit.append(current + [(nr, nc)])
            total += len(nines)
    return total

test_data = parser("010_test.txt")
assert p1(test_data) == 36
actual_data = parser()
print(p1(actual_data))

test_data = parser("010_test.txt")
assert p2(test_data) == 81
actual_data = parser()
print(p2(actual_data))


