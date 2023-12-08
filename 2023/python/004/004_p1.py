from itertools import zip_longest

# part 1
totaal = 0
with open('004.txt', 'r') as file:
    for line in file:
        wins, owns = line.strip().split(": ")[1].split(" | ")
        wins = wins.split()
        owns = owns.split()
        same = sum((own in wins for own in owns if own != ''))
        totaal += int(2 ** (same - 1))
        """
            0 duplicates    2 ^ -1 = 0.5
            1 duplicate     2 ^ 0 = 1
            2 duplicates    2 ^ 1 = 2
            3 duplicates    2 ^ 2 = 4
            .....
        """
print(totaal)


