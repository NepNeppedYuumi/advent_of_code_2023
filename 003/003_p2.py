from re import finditer


def parser(file="007.txt"):
    with open(file, 'r') as file:
        data = file.read().split('\n')
        return data


def find_num(data, x, y):
    string = data[x]
    start_y = y
    end_y = y
    while string[start_y].isdecimal() and start_y != -1:
        start_y -= 1
    try:
        while string[end_y].isdecimal():
            end_y += 1
    except IndexError:
        end_y += 1
    return string[start_y+1:end_y]


def part_two(data):
    total_sum = 0
    for i, line in enumerate(data):
        skip_till = - 1
        for j, char in enumerate(data[i]):
            if not char.isdecimal() or skip_till > j:
                continue
            total_characters = 0
            big_num = ""
            for num in line[j:]:
                if not num.isdecimal():
                    break
                big_num += num
                total_characters += 1
            string = ''
            gear = False
            gear_nums = ''
            for x, section in enumerate(data[max(0, i - 1):min(i + 2, len(data))], start=max(0, i - 1)):
                for y, char_ in enumerate(section[max(0, j - 1):min(len(line),
                                                       j + total_characters + 1)], start=max(0, j - 1)):
                    string += char_
                    if not char_.isdecimal() and char_ != '.':
                        slices = [part[max(0, y - 1):min(len(line), y + 2)] for part in data[max(0, x - 1):min(x + 2, len(data))]]
                        slice_string = '.'.join(slices).replace(char_, '.')

                        nums = [num for num in slice_string.split('.') if num.isdecimal()]
                        if len(nums) > 1:
                            gear = True
                            print(slice_string)
                            num_indexes = [m.start() for m in finditer('|'.join(nums),slice_string)]
                            num_indexes = [(max(0, min(len(data), (num_index // 4) - 1  + x)),
                                            max(0, min(len(line), (num_index % 4) - 1  + y))) for num_index in num_indexes]
                            gear_nums = [find_num(data, *coords) for coords in num_indexes]
                            print(nums, num_indexes, gear_nums)
                            gear = True
                    if gear:
                        break
                if gear:
                    break
            if not gear:
                continue
            total_sum += int(gear_nums[0]) * int(gear_nums[1])
            skip_till = j + total_characters
    print(int(total_sum / 2))


data_ = parser()
part_two(data_)