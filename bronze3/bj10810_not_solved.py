import collections

a, b = map(int, input().split(' '))
li = {}
for i in range(a):
    li[i+1] = 0

for _ in range(b):
    i, j, k = map(int, input().split(' '))
    for _i in range(i, j+1):
        print(_i)

print(li.values())
