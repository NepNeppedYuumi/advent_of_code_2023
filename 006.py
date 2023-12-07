
# part 1
# with open('006', 'r') as file:
#     times, distances = file.read().split('\n')
# times, distances = times[11:].split(), distances[11:].split()
# product = 1
# for time, distance in zip(map(int, times), map(int, distances)):
#     counter = 0
#     for x in range(1, time):
#
#         if x * (time - x) > distance:
#             print(x, x * (time - x), distance)
#             counter += 1
#     else:
#         print(counter)
#         product *= counter
# print(product)


# part 2
with open('006', 'r') as file:
    times, distances = file.read().split('\n')
to_number = lambda x: int(x[11:].replace(' ', ''))
time, distance = to_number(times), to_number(distances)

counter = 0
for x in range(1, time):

    if x * (time - x) > distance:
        start = x
        break

for x in range(time, 1, -1):

    if x * (time - x) > distance:
        end = x
        break


print(end - start + 1)


with open('006', 'r') as file:
    times, distances = file.read().split('\n')
to_number = lambda x: int(x[11:].replace(' ', ''))
time, distance = to_number(times), to_number(distances)

counter = 0
for x in range(1, time):

    if x * (time - x) > distance:
        counter += 1
print(counter)