import sys

na = []
for i in range(0, num := int(input())):
    na.append(int(sys.stdin.readline()))


for i in range(len(na)):
    for j in range(i+1, len(na)):
        if na[i] > na[j]:
            na[i], na[j] = na[j], na[i]

for i in na:
    print(i)