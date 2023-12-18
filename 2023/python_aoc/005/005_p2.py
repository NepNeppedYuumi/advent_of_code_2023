

# part 2
with open('005.txt', 'r') as file:
    seeds = file.readline().split(": ")[1].rstrip().split(' ')
    seeds = list(map(int, seeds))
    lowest = []
    print(seeds)
    seed_range = []
    for i in range(0, len(seeds), 2):
        seed_range.append(range(seeds[i], seeds[i+1] + seeds[i]))

    instructions = file.read().strip().split("\n\n")
    for y, i in enumerate(instructions):
        print(
            f"instruction {int(y)} out of 6")
        print(seed_range)
        i = i.split("\n")
        i_name = i[0]
        maps = []
        for new, old, length in map(str.split, i[1:]):
            new, old, length = int(new), int(old), int(length)
            ra = (old - new, old, old + length)
            maps.append(ra)
        print(maps)
        new_ranges = []
        for diff, old_start, old_end in maps:
            change_map = range(old_start, old_end)
            current_index = 0
            while current_index < len(seed_range):
                current_range = seed_range[current_index]
                if not current_range:
                    print(current_range)
                    seed_range.pop(current_index)
                    continue
                first = current_range[0]
                last = current_range[-1]
                if first in change_map or last in change_map:
                    # print(current_range, change_map, diff, seed_range)
                    seed_range.pop(current_index)
                    if first not in change_map:
                        first_id = current_range.index(change_map[0])
                        seed_range.append(current_range[:first_id])

                        new_ranges.extend([range(current_range[first_id] - diff, last - diff)])
                    elif last not in change_map:
                        last_id = current_range.index(change_map[-1]) + 1

                        seed_range.append(current_range[last_id:])
                        new_ranges.extend([range(first - diff, current_range[last_id] - diff)])
                    else:
                        new_ranges.extend(
                            [range(first - diff, first - diff + len(current_range))]
                        )

                    current_index -= 1

                elif change_map[0] in current_range and change_map[-1] in current_range:
                    # print(change_map, diff, seed_range)
                    this_start = current_range.index(change_map[0])
                    seed_range.append(current_range[:this_start])
                    seed_range.append(current_range[this_start+len(change_map):])
                    range_slice = current_range[this_start:this_start+len(change_map)]
                    new_ranges.append(range(range_slice[0] - diff, range_slice[-1] - diff)
                        )
                    seed_range.pop(current_index)
                    current_index -= 1

                elif change_map[0] in current_range or change_map[-1] in current_range:
                    raise BrokenPipeError
                else:
                    pass
                current_index += 1

        seed_range.extend(new_ranges)

    # lowest.append(min(seed_range, key=lambda x: x[0])[0])
    lowest.extend(seed_range)
    actual_lowest = min(lowest, key=lambda x:x[0])
    print(lowest)
    print(actual_lowest[0])
