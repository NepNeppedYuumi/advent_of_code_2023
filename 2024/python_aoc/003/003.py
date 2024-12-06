import re


def parser(file="input.txt"):
    with open(file, 'r') as file:
        data = file.read()
        return data


def part_one(data):
    matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data)
    total = 0
    for match in matches:
        a, b = match.strip("mul()").split(",")
        total += int(a) * int(b)
    print(total)
    return total


def part_two(data):
    matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", data)
    total = 0
    do = True
    for match in matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        else:
            if do is not True:
                continue
            a, b = match.strip("mul()").split(",")
            total += int(a) * int(b)
    print(total)
    return total

if __name__ == '__main__':
    # data_ = parser(file="003_test.txt")
    # part_one(data_)
    data_ = parser()
    part_one(data_)
    
    data_ = parser()
    total = part_two(data_)
    assert total == 84893551

