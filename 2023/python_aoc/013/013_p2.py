

def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        batches = file.read().split('\n\n')
        data = []
        for i, lines in enumerate(batches):
            data.append(lines.splitlines())
    return data


def find_breakline(pat):
    total = [0]
    for i, y in enumerate(pat[:-1], start=1):
        diffed = True
        if (amount := sum(a == b for a, b in zip(y, pat[i]))) >= len(y) - int(diffed):
            # print(amount, i)
            if amount != len(y):
                diffed = False
            try:
                j = 1
                while i - 1 - j >= 0:
                    if (sub := sum(a == b for a, b in zip(pat[i - 1 - j], pat[j + i]))) >= len(y) - int(diffed):
                        # print(sub, len(y), j)
                        if sub != len(y):
                            diffed = False
                        j += 1
                    else:
                        # print("we breaking", sub, len(y))
                        break
                else:
                    print(i - 1 - j)
                    if i - 1 - j < 0:
                        raise IndexError
            except IndexError:
                print(diffed)
                if diffed is True:
                    continue
                return i
    return max(total)


def p1(data):
    total = 0
    no_mirror = 0
    for pat in data:
        horizontal = find_breakline(pat)
        vertical = find_breakline(list(zip(*pat)))
        if horizontal != 0 and vertical != 0:
            raise BrokenPipeError
        if horizontal == vertical == 0:
            print("\n".join(pat))
            raise BlockingIOError
        total += vertical
        total += 100 * horizontal
    print(total)
    print(no_mirror)
    return total


test_data = parser("013_test.txt")
assert p1(test_data) == 400
# test_data = parser("test4")
# assert p2(test_data) == 1600
actual_data = parser()
print(p1(actual_data))