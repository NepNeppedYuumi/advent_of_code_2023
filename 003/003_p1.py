from re import finditer


def parser(file="007.txt"):
    with open(file, 'r') as file:
        data = file.read().split('\n')
        return data


def part_one(data):
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
            lijst = []
            for section in data[max(0, i-1):min(i+2, len(data))]:
                lijst.append(section[max(0, j-1):min(len(line), j+total_characters+1)])
            if any(not chars.isdecimal() and chars != '.' for chars in ''.join(lijst)):
                total_sum += int(big_num)
            skip_till = j + total_characters
    print(total_sum)


if __name__ == '__main__':
    data_ = parser(file="003_test.txt")
    part_one(data_)
    data_ = parser()
    part_one(data_)

