from datetime import datetime


# part 1
with open('005.txt', 'r') as file:
    seeds = file.readline().split(": ")[1].rstrip().split(' ')
    seeds = list(map(int, seeds))
    print(seeds)
    instructions = file.read().strip().split("\n\n")
    for i in instructions:
        i = i.split("\n")
        i_name = i[0]
        new_seeds = []
        maps = []
        for new, old, length in map(str.split, i[1:]):
            new, old, length = int(new), int(old), int(length)
            ra = (old - new, old, old + length)
            maps.append(ra)
        for seed in seeds[:]:
            for diff, start, stop in maps:
                if seed in range(start, stop):
                    new_seeds.append(seed - diff)
                    seeds.remove(seed)
        seeds.extend(new_seeds)
        print(seeds)
    print()
    print(seeds)
    print(min(seeds))

