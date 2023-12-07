

def read(file_name, slice_size):
    counter = 0
    with open(file_name, 'r') as file:
        file_data = tuple(map(int, file))
    depth = sum(file_data[0: slice_size])
    for i in range(1, len(file_data) - slice_size + 1):
        new_depth = sum(file_data[i: i + slice_size])
        if new_depth > depth:
            counter += 1
        depth = new_depth
    return counter


print(read("day1_test.txt", 1))
print(read("day1.txt", 1))
print(read("day1_test.txt", 3))
print(read("day1.txt", 3))

