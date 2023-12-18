

# part 1
total_count = 0
with open('001.txt', 'r') as file:
    for line in file:
        line = [num for num in line if num.isdecimal()]
        number = int(line[0] + line[-1])
        print(number)
        total_count += number
print(total_count)


