whil = [None]*4

lijst = [i for _ in whil if (b:=((i:=input("geef inp: ")).isdigit()), whil.append(None) if not b else None)[0]]
print(lijst)