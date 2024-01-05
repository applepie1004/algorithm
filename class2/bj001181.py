_dict = {}

for _ in range(int(input())):
    b = input()
    _dict[b] = len(b)

sorted_dict = sorted(_dict.items(), key=lambda item: [item[1], item[0]])

for i in range(len(sorted_dict)):
    print(sorted_dict[i][0])
