

data = []
voorgerecht = {}
hoofdgerecht = {}
nagerecht = {}


def string(dictionary):
    st = ''
    dictionary = sorted([(a, b) for a, b in dictionary.items()], key= lambda x: -x[1])
    for key, item in dictionary:
        st += f"{key}: {item}\n"
    return st


with open("Kerstdiner Exon 2023.csv", 'r') as file:
    file.readline()
    file.readline()
    for line in file:
        line = line.split('","')
        v = line[3].strip('*"')
        h = line[4].strip('"*')
        n = line[5].strip('*"\n')
        voorgerecht[v] = voorgerecht.get(v, 0) + 1
        hoofdgerecht[h] = hoofdgerecht.get(h, 0) + 1
        nagerecht[n] = nagerecht.get(n, 0) + 1


with open("info voor versturen.txt", 'w') as file:
    file.write("Voorgerecht\n")
    file.write(string(voorgerecht))
    file.write('\n\n')

    file.write("Hoofdgerecht\n")
    file.write(string(hoofdgerecht))
    file.write('\n\n')

    file.write("Nagerecht\n")
    file.write(string(nagerecht))
