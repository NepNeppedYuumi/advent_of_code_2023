from itertools import combinations
from collections import defaultdict


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read()
    return lines


def p1(data):
    a, b = data.split("\n\n")
    order = []
    total = 0
    for line in a.split("\n"):
        first, later = line.split("|")
        order.append((first, later))
    
    for line in b.split("\n"):
        for f, l in order:
            try:
                if line.index(l) < line.index(f):
                    break
            except ValueError:
                pass
        else:
            line = line.split(",")
            print(line)
            i = len(line) // 2
            print(i, line[i])
            total += int(line[i])
    print(total)
    return total


def p2(data):
    a, b = data.split("\n\n")
    order = defaultdict(lambda :[])
    total = 0
    for line in a.split("\n"):
        first, later = line.split("|")
        order[first].append(later)
        
    for line in b.split("\n"):
        line = line.split(",")
        bad = False
        
        for key in order.keys():
            for value in order[key]:
                if key not in line or value not in line:
                    continue
                ki = line.index(key)
                vi = line.index(value)
                
                if ki > vi:
                    bad = True
                    line.pop(ki)
                    line.insert(vi, key)
        if bad:
            i = len(line) // 2
            total += int(line[i])
    print(total)
    return total
    

# test_data = parser("005_test.txt")
# assert p1(test_data) == 143
# actual_data = parser()
# print(p1(actual_data))

lijst = [1]


lijst.insert(0, "a")
print(lijst)

test_data = parser("005_test.txt")
assert p2(test_data) == 123
actual_data = parser()
print(p2(actual_data))

