import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))

MAX = 0
sorted_A = sorted(A)  # 병합정렬, 최악의 경우에도 시간복잡도 O(NlogN)을 보장

print(A, sorted_A)

for i in range(N):
    num = sorted_A[i][1] - i
    if MAX < num:
        MAX = num

print(MAX + 1)


