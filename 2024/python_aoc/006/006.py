from itertools import combinations
from collections import defaultdict


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return lines


def p1(data):
    pos = None
    for i, row in enumerate(data):
        if "^" in row:
            pos = (i, row.index("^"))
            break
    
    visited = {pos}
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    dir_i = 0
    while True:
        r, c = pos
        nr, nc = r + directions[dir_i][0], c + directions[dir_i][1]
        if nr < 0 or nr >= len(data) or nc < 0 or nc >= len(data[0]):
            break
        if data[nr][nc] == "#":
            dir_i = (dir_i + 1) % 4
            continue
        pos = (nr, nc)
        print(pos)
        visited.add(pos)
        
    total = len(visited)
    print(total)
    return total


def p2(data):
    start_pos = None
    for i, row in enumerate(data):
        if "^" in row:
            start_pos = (i, row.index("^"))
            break
    
    total = 0
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col != ".":
                continue
            
            data[i] = data[i][:j] + "#" + data[i][j + 1:]
            
            pos = start_pos
            directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
            dir_i = 0
            visited = {(pos, directions[dir_i])}
            while True:
                r, c = pos
                direction = directions[dir_i]
                nr, nc = r + direction[0], c + direction[1]
                if nr < 0 or nr >= len(data) or nc < 0 or nc >= len(data[0]):
                    break
                if data[nr][nc] == "#":
                    dir_i = (dir_i + 1) % 4
                    continue
                pos = (nr, nc)
                
                if (pos, direction) in visited:
                    total += 1
                    break
                
                visited.add((pos, direction))
                
            data[i] = data[i][:j] + "." + data[i][j + 1:]
    
    print(total)
    return total
    
    
    total = 0
    return total


test_data = parser("006_test")
assert p1(test_data) == 41
actual_data = parser()
print(p1(actual_data))


test_data = parser("006_test")
assert p2(test_data) == 6
actual_data = parser()
print(p2(actual_data))

