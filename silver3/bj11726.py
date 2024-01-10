import sys
input = sys.stdin.readline

N = int(input())
D = [1] * (N + 1)

for i in range(2, N + 1):
    D[i] = D[i-1] + D[i-2]

print(D[N] % 10007)

