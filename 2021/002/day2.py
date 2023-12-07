

class Position:

    def __init__(self, file_name):
        self.horizontal = 0
        self.depth = 0
        self.apply_changes(file_name)

    def __str__(self):
        return f"multiplied it's {self.horizontal * self.depth}"

    def increase_horizontal(self, horizontal):
        self.horizontal += horizontal

    def increase_depth(self, depth):
        self.depth += depth

    def apply_changes(self, file_name):
        change_dictionary = {
            'forward': lambda x: self.increase_horizontal(int(x)),
            'up': lambda x: self.increase_depth(int("-"+x)),
            'down': lambda x: self.increase_depth(int(x))
        }
        with open(file_name, 'r') as file:
            for direction, amount in map(lambda x: x.split(' '), file):
                func = change_dictionary[direction]
                func(amount)


class Position2:

    def __init__(self, file_name):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        self.apply_changes(file_name)

    def __str__(self):
        return f"multiplied it's {self.horizontal * self.depth}"

    def increase_horizontal(self, x):
        self.horizontal += x
        self.depth += (self.aim * x)

    def inc_aim(self, aim):
        self.aim += aim

    def apply_changes(self, file_name):
        change_dictionary = {
            'forward': lambda x: self.increase_horizontal(int(x)),
            'up': lambda x: self.inc_aim(-int(x)),
            'down': lambda x: self.inc_aim(int(x))
        }
        with open(file_name, 'r') as file:
            for direction, amount in map(lambda x: x.split(' '), file):
                func = change_dictionary[direction]
                func(amount)


print(Position("day2_test.txt"))
print(Position("day2.txt"))
print(Position2("day2_test.txt"))
print(Position2("day2.txt"))