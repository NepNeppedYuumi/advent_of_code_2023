

with open('001.txt', 'r') as file:
    lines = []
    for line in file:
        line2 = ''
        for i in range(0, len(line)):
            if line[i].isnumeric():
                line2 += line[i]
                continue
            for y, value in enumerate(('one','two','three','four',
                                       'five','six','seven','eight','nine'), start=1):
                if line[i:i + 5].startswith(value):
                    line2 += str(y)
                    break
        line = int(line2[0] + line2[-1])
        lines.append(line)
    print(sum(lines))
