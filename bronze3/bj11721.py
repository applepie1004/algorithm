txt = input()

for i in range(0, len(txt), 10):
    if i + 10 < len(txt):
        print(txt[i:i + 10])
    else:
        print(txt[i:])
