from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().strip().split(',')
    return lines


def p1(data):
    total = 0
    boxes = {i: [] for i in range(256)}
    for word in data:
        box_i = 0
        for c in word.strip("0123456789-="):
            box_i += ord(c)
            box_i *= 17
            box_i = box_i % 256
        current_box = boxes[box_i]
        if '-' in word:
            word = word.split('-')
            for i, content in enumerate(current_box):
                if word[0] == content[0]:
                    current_box.pop(i)
                    break
        else:
            word = word.split('=')
            for i, content in enumerate(current_box):
                if word[0] == content[0]:
                    current_box[i] = word
                    break
            else:
                current_box.append(word)
        print(current_box)
    for box, lenses in boxes.items():
        current = 0
        for i, lens in enumerate(lenses, start=1):
            print(lens)
            current += (box + 1) * i * int(lens[1])
        total += current
    print(boxes)
    print(total)
    return total


test_data = parser("015_test.txt")
assert p1(test_data) == 145
actual_data = parser()
print(p1(actual_data))