with open('001.txt', 'r') as file:
    lines = []
    dicto = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    count = -1
    line_num = 3
    for line in file:
        count += 1
        if count < line_num:
            continue
        line2 = ''
        print(line)
        for i in range(0, len(line)):
            if line[i].isnumeric():
                line2 += line[i]
                continue
            for key, value in dicto.items():
                if line[i:i + 5].startswith(key):
                    line2 += str(value)
        line = line2
        line = line[0] + line[-1]
        line = int(line)
        lines.append(line)
        print(line)
        if count == line_num:
            break
    print(sum(lines))
