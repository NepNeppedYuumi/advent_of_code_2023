

COLOURS = ['red', 'green', 'blue']
COLOUR_VALUES = [12, 13, 14]

# part 1
with open('002.txt', 'r') as file:
    total = 0
    for game in file:
        game_id, draws = game.strip().split(': ')
        draws = draws.split('; ')
        impossible = False
        for time in draws:
            colours = time.split(', ')
            for colour in colours:
                num, col = colour.split(' ')
                colour_index = COLOURS.index(col)
                if COLOUR_VALUES[colour_index] < int(num):
                    impossible = True
        if impossible:
            continue
        total += int(game_id.split(' ')[-1])
print(total)



