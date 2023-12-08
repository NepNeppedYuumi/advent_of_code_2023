

with open('008.txt', 'r') as file:
    options = {}
    directions, all_options = file.read().split('\n\n')
    all_options = all_options.split('\n')
    for line in all_options:
        options[line[0:3]] = line[7:10], line[12:15]

current_position = "AAA"
steps = 0
option_map = "LR"
while current_position != 'ZZZ':
    direction = option_map.index(directions[steps % len(directions)])
    steps += 1
    current_position = options[current_position][direction]
    print(current_position)
print(current_position)
print(steps)