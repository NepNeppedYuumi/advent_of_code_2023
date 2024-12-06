from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return lines


def p1(data):
    total = 0
    for rep in data:
        rep = [int(x) for x in rep.split()]
        if not (
                all(a <b for a, b in zip(rep, rep[1:]))
                or all(a > b for a, b in zip(rep, rep[1:]))
        ):
            continue
        for i in range(1, len(rep)):
            diff = rep[i - 1] - rep[i]
            if abs(diff) not in (1, 2, 3):
                break
        else:
            total += 1
    return total


def flaw_finder(rep):
    jump = []
    up = []
    down = []
    for i in range(1, len(rep)):
        diff = rep[i - 1] - rep[i]
        if abs(diff) > 3:
            jump.append(i)
        if abs(diff) == 0:
            jump.append(i)
        if diff < 0:
            up.append(i)
        if diff > 0:
            down.append(i)
    return jump, up, down


def p2(data):
    total = 0
    for rep in data:
        rep = [int(x) for x in rep.split()]
        
        jump, up, down = flaw_finder(rep)

        if len(up) < len(down):
            direction = up
        else:
            direction = down
        
        if len(direction) == len(jump) == 0:
            total += 1
            continue
        
        if len(direction) >1 or len(jump) > 1:
            continue
        if len(direction) >= 1:
            pos = direction[0]
        elif len(jump) >= 1:
            pos = jump[0]
        
        increase = False
        for i in range(pos-1, pos+1):
            crep = rep.copy()
            crep.pop(i)
            jump, up, down = flaw_finder(crep)
        
            if len(up) < len(down):
                direction = up
            else:
                direction = down
                
            if len(direction) == len(jump) == 0:
                increase = True
                break
        if increase:
            total += 1
    return total



test_data = parser("002_test.txt")
assert p1(test_data) == 2
actual_data = parser()
print(p1(actual_data))

test_data = parser("002_test.txt")
assert p2(test_data) == 4
actual_data = parser()
print(p2(actual_data))

