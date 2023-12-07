from collections import Counter

# part 1
with open('input.txt', 'r') as file:
    data = []
    for line in file:
        hand, bid = line.strip().split()
        data.append((hand, int(bid)))


def sort_value(hand):
    order = "23456789TJQKA"
    cardies = hand[0]
    hand = hand[0]
    cards = Counter(hand)
    card_amounts = list(cards.values())
    max_cards = max(card_amounts)
    hand_value = 0
    if max_cards == 5:
        hand_value += len(order) * (10 ** 19)
    elif max_cards == 4:
        hand_value += len(order) * (10 ** 18)
    elif 3 == max_cards and 2 in card_amounts:
        hand_value += len(order) * (10 ** 17)
    elif max_cards == 3:
        hand_value += len(order) * (10 ** 16)

    elif card_amounts.count(2) == 2:
        hand_value += len(order) * (10 ** 15)

    elif max_cards == 2:
        hand_value += len(order) * (10 ** 14)
    else:
        hand_value += (len(order) * (10 **12)) * order.index(hand[0])

    for i, card in enumerate(hand):
        hand_value += ((len(order) * (10 ** ((len(hand) * 2) - (i * 2)))) * order.index(card))

    return hand_value
# jus_cards = [thing[0] for thing in data]
# if any((jus_cards.count((mmh := thing)) != 1 for thing in jus_cards)):
#     print("bro what")
#     print(mmh)
#     exit()


data = sorted(data, key=sort_value)
print(data)
total = 0
for i, hand in enumerate(data, start=1):
    cards, bid = hand
    total += bid * i
print(total)


