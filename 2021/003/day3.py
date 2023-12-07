

def option1(file_name):
    with open(file_name, 'r') as file:
        file_data = file.read().strip().split()
    gamma = ''
    for column in zip(*file_data):
        gamma += max(set(column), key=column.count)
    epsilon = int(gamma.translate(str.maketrans("10", "01")), 2)
    gamma = int(gamma, 2)
    return epsilon * gamma


def option2(file_name):
    with open(file_name, 'r') as file:
        file_data = file.read().strip().split()
    oxygen_list = file_data
    co2_list = file_data.copy()
    for i in range(len(file_data[0])):
        if len(oxygen_list) > 1:
            ox_char_list = [element[i] for element in oxygen_list]
            ox_c = '1'
            if ox_char_list.count(ox_c) < len(ox_char_list) / 2:
                ox_c = '0'
            oxygen_list = [
                oxygen_list[element] for element in range(len(oxygen_list))
                if oxygen_list[element][i] == ox_c]
        if len(co2_list) > 1:
            co2_char_list = [element[i] for element in co2_list]
            co2_c = '0'
            if co2_char_list.count(co2_c) > len(co2_char_list) / 2:
                co2_c = '1'
            co2_list = [
                co2_list[element] for element in range(len(co2_list))
                if co2_list[element][i] == co2_c]
    return int(*oxygen_list, 2) * int(*co2_list, 2)


print(option1('day3_test.txt'))
print(option1('day3.txt'))
print(option2('day3_test.txt'))
print(option2('day3.txt'))


