import sys
input = sys.stdin.readline

na = []
for _ in range(0, int(input())):
    na.append(int(input()))

na.sort()

for i in na:
    print(i)