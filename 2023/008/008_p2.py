

with open('008.txt', 'r') as file:
    options = {}
    directions, all_options = file.read().split('\n\n')
    all_options = all_options.split('\n')
    for line in all_options:
        options[line[0:3]] = line[7:10], line[12:15]

current_positions = [key for key in options.keys() if key.endswith("A")]
z_at_traceback = [[] for _ in range(len(current_positions))]
print(current_positions)
steps = 0
option_map = "LR"
finished = False


while any(len(i) < 1 for i in z_at_traceback):
    direction = option_map.index(directions[steps % len(directions)])
    steps += 1
    for i, position in enumerate(current_positions):
        current_positions[i] = options[position][direction]
        if current_positions[i].endswith("Z"):
            z_at_traceback[i].append(steps)


z_at_traceback = [trace[0] for trace in z_at_traceback]
print(z_at_traceback)


from math import gcd
a = z_at_traceback  #will work for an int array of any length
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)