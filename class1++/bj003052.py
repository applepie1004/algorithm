nl = {}
for i in range(10):
    if i not in nl:
        nl[str(int(input()) % 42)] = 1
print(len(nl))

