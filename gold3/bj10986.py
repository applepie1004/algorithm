N, M = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
S = []
C = [0] * M
_sum = 0
answer = 0

for i in A:
    _sum += i
    S.append(_sum % M)

for i in range(N):
    if S[i] == 0:
        answer += 1
    C[S[i]] += 1

for i in range(M):
    if C[i] > 1:
        answer = answer + (C[i] * (C[i] - 1) / 2)

print(int(answer))


from math import comb


def solution(M: int, nums: list[int]) -> int:
    total = 0
    cnt = [0] * M
    cnt[0] = 1
    for num in nums:
        total = (total + num) % M
        cnt[total] += 1
    value = 0
    for v in cnt:
        value += comb(v, 2)
    return value


N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = solution(M, nums)
print(ans)
