from itertools import combinations
from queue import PriorityQueue


INFINITY = float('inf')


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return lines


def p1(data):
    nodes = set()
    unvisited = set()
    costs = {}
    distance_from_start = {}
    angle_and_angle_count = {}
    previous = {}

    start_node = (0, 0)
    start_info = ((0, 0), (0, 1), 0)
    unvisited.add(start_info)
    distance_from_start[start_info] = 0
    queue = PriorityQueue()
    queue.put((0, *start_info))

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            nodes.add((i, j))
            costs[(i, j)] = int(char)
            # angle_and_angle_count[(i, j)] = None
            if (i, j) == start_node:
                continue
            for angle in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                for a in range(1, 11):
                    node_info = ((i, j), angle, a)
                    unvisited.add(node_info)
                    distance_from_start[node_info] = INFINITY
                    previous[node_info] = None

    end_node = (i, j)
    ended_at = None
    print("yo")
    while queue:
        distance, *current_node = queue.get()

        current_node = tuple(current_node)

        if (current_distance := distance_from_start[current_node]) == INFINITY:
            break
        (x, y), current_angle, angle_count = current_node
        dx, dy = current_angle

        future_count = angle_count + 1
        if angle_count == 0:
            neighbour_angles = [(dx, dy), (dy, dx), (-dy, -dx)]
        elif future_count > 10:
            neighbour_angles = [(dy, dx), (-dy, -dx)]
        elif future_count > 4:
            neighbour_angles = [(dx, dy), (dy, dx), (-dy, -dx)]
        else:
            neighbour_angles = [(dx, dy)]

        for dx, dy in neighbour_angles:
            n_count = 1 + (current_angle == (dx, dy)) * angle_count
            # if n_count > 3:
            #     continue
            n_node = (x + dx, y + dy)
            if n_node not in nodes or n_node == start_node:
                continue
            n_node_info = (n_node, (dx, dy), n_count)
            new_path = current_distance + costs[n_node]
            if new_path < distance_from_start[n_node_info]:
                distance_from_start[n_node_info] = new_path
                previous[n_node_info] = current_node
                queue.put((new_path, *n_node_info))
        if current_node[0] == end_node and current_node[2] >= 4:
            print(current_node[0], end_node)
            print("we ending it")
            ended_at = current_node
            break
    actual_path = [ended_at]
    current_node = ended_at
    while current_node[0] != start_node:
        current_node = previous[current_node]
        actual_path.append(current_node)
    print(actual_path[::-1])
    string = ""
    string2 = ""
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if any((i, j) == (this := x)[0] for x in actual_path):
                string += '>'
                string2 += str(this[2]).replace('10', 'T')
            else:
                string += char
                string2 += ' '
        string += '\n'
        string2 += '\n'
    with open("part2_result", 'w') as file:
        file.write(string)
        file.write('\n\n\n')
        file.write(string2)
    print(distance_from_start[ended_at])
    return distance_from_start[ended_at]


test_data = parser("017_test.txt")
assert p1(test_data) == 94
test_data = parser("part2_test")
assert p1(test_data) == 71
actual_data = parser()
print(p1(actual_data))