

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
        if y == pat[i]:
            if y == "####.###.#...#.":
                print("yes we got here!")
            try:
                j = 1
                while pat[i - 1 - j] == pat[j + i] and i - 1 - j >= 0:
                    if y == "####.###.#...#.":
                        print("we in the while loop now")
                    j += 1
                else:
                    if i - 1 - j < 0:
                        raise IndexError
            except IndexError:
                # return i
                if y == "####.###.#...#.":
                    print(f"okay so this is {i} here")
                total.append(i)
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
            raise BlockingIOError
        total += vertical
        total += 100 * horizontal
    print(total)
    print(no_mirror)
    return total


test_data = parser("013_test.txt")
assert p1(test_data) == 405
test_data = parser("test4")
assert p1(test_data) == 1600
actual_data = parser()
print(p1(actual_data))