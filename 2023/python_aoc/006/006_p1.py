

# part 1
with open('006', 'r') as file:
    times, distances = file.read().split('\n')
times, distances = times[11:].split(), distances[11:].split()
product = 1
for time, distance in zip(map(int, times), map(int, distances)):
    counter = 0
    for x in range(1, time):

        if x * (time - x) > distance:
            print(x, x * (time - x), distance)
            counter += 1
    else:
        print(counter)
        product *= counter
print(product)
