

# part 1
def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        data = []
        for i, line in enumerate(lines):
            data.append( [int(num) for num in line.split()])
    return data


def p2(data):
    total = 0
    for i, seq in enumerate(data):
        new_sequences = [seq]
        while not all(s == 0 for s in new_sequences[-1]):
            to_append = []
            for j, sseq in enumerate(new_sequences[-1][:-1]):
                diff = new_sequences[-1][j+1] - sseq
                to_append.append(diff)
            new_sequences.append(to_append)

        new_sequences[-1].insert(0, 0)
        for j, rseq in enumerate(new_sequences[-2::-1], start=2):
            new_num = rseq[0] - new_sequences[-j+1][0]
            rseq.insert(0, new_num)
        total += new_sequences[0][0]
    return total


test_data = parser("009_test.txt")
assert p2(test_data) == 2
actual_data = parser()
print(p2(actual_data))