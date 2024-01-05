import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
S = [0]
_sum = 0

for i in range(n):
    _sum += nums[i]
    S.append(_sum)

print(S)

for i in range(m):
    a, b = map(int, input().split())
    print(S[b] - S[a - 1])
