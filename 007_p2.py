from collections import Counter


class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.counter = Counter(self.cards)
        items = sorted(list(self.counter.items()), key=lambda x: x[1], reverse=True)
        values = list(self.counter.values())
        self.max = items[0][1]
        if (j := self.counter['J']) and len(values) > 1:
            if j < self.max:
                self.max += j
            elif j > self.max:
                self.max += items[1][1]
            else:
                self.max += next((i[1] for i in items if i[0] != 'J'))
        if not j and (self.max == 3 and (2 in values) or values.count(2) == 2):
            self.max += 0.5
        if j == 1 and values.count(2) == 2:
            print(self.cards, self.max)
            self.max += 0.5

    def __lt__(self, other: "Hand"):
        order = "J23456789TQKA"
        if self.max > other.max:
            return False
        elif self.max < other.max:
            return True
        else:
            for own_card, other_card in zip(self.cards, other.cards):
                if order.index(own_card) > order.index(other_card):
                    return False
                elif order.index(own_card) < order.index(other_card):

                    return True
            else:
                print((self.cards, self.bid), (other.cards, other.bid))
                raise BrokenPipeError

    def __repr__(self):
        return self.cards


# part 2
with open('input.txt', 'r') as file:
    data = []
    for line in file:
        hand, bid = line.strip().split()
        data.append(Hand(hand, int(bid)))


data.sort()
print(data)
total = 0
for i, hand in enumerate(data, start=1):
    total += hand.bid * i
print(total)

exit()
# part 2
with open('input.txt', 'r') as file:
    data = []
    for line in file:
        hand, bid = line.strip().split()
        data.append(Hand(hand, int(bid)))


data.sort()
print(data)
total = 0
for i, hand in enumerate(data, start=1):
    total += hand.bid * i
print(total)