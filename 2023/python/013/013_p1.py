

def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        data = []
        for i, line in enumerate(lines):
            data.append( [int(num) for num in line.split()])
    return data


def p1(data):
    return None


test_data = parser("010_test.txt")
assert p1(test_data) == 114
actual_data = parser()
print(p1(actual_data))