from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read()
    return lines


def p1(data):
    total = 0
    line_length = data.index("\n")
    print(line_length)
    word = "XMAS"
    directions = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    )
    for i, c in enumerate(data):
        if c != word[0]:
            continue
        for (x, y) in directions:
            for j, subc in enumerate(word[1:], start=1):
                try:
                    ni = i + (j * x * (line_length + 1)) + (j * y)
                    if ni < 0:
                        break
                    nchar = data[ni]
                    if nchar != subc:
                        break
                except:
                    break
            else:
                total += 1
    print(total)
    return total

def p2(data):
    total = 0
    line_length = data.index("\n")
    for i, c in enumerate(data):
        if c not in "MS":
            continue
        try:
            str1 = c + data[i + (1 * (line_length + 1)) + 1] + \
                    data[i + (2 * (line_length + 1)) + 2]
            str2    = data[i + 2] + data[(i + 2) + (1 * (line_length + 1)) - 1] + \
                    data[(i + 2) + (2 * (line_length + 1)) - 2]
            if (str1 == str2 or str1[::-1] == str2) and str1 in ("MAS", "SAM"):
                total +=1
        except Exception as e:
            continue
    return total

#
# test_data = parser("004_test.txt")
# assert p1(test_data) == 18
# actual_data = parser()
# print(p1(actual_data))

test_data = parser("004_test.txt")
assert p2(test_data) == 9
actual_data = parser()
print(p2(actual_data))

