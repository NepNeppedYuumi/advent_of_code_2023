from functools import reduce


# part 2

COLOURS = ['red', 'green', 'blue']
COLOUR_VALUES = [12, 13, 14]


with open('002.txt', 'r') as file:
    total = 0
    for line in file:
        g, line = line.strip().split(': ')
        line = line.split('; ')
        game_max = [0, 0, 0]
        for row in line:
            thing = row.split(', ')
            for colour in thing:
                num, col = colour.split(' ')
                num = int(num)
                colour_index = COLOURS.index(col)
                if game_max[colour_index] < num:
                    game_max[colour_index] = num
        total += reduce(lambda x, y: x * y, game_max)
print(total)