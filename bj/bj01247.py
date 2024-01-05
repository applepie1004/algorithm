from sys import stdin

for i in range(3):
    _sum = 0
    for _ in range(int(stdin.readline())):
        _sum += int(stdin.readline())
    print('0' if _sum == 0 else '-' if _sum < 0 else '+')
