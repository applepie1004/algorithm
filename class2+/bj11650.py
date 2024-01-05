arr = []

for _ in range(0, int(input())):
    arr.append(list(map(int, input().split(' '))))

arr.sort()

for a in arr:
    print(a[0], a[1])
