s = input()
atoz = list(range(ord('a'), ord('z')+1))
atoz_int = [-1 for num in range(len(atoz))]

for i in atoz:
    idx = s.find(str(chr(i)))
    atoz_int[atoz.index(i)] = idx

print(" ".join(map(str, atoz_int)))

