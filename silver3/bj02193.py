import sys
input = sys.stdin.readline

N = int(input())

D = [[0 for j in range(2)] for i in range(N+1)]
D[1][1] = 1
D[1][0] = 0

for i in range(2, N+1):
    D[i][0] = D[i - 1][1] + D[i - 1][0]  # i의 길이에서 끝이 0으로 끝나는 이친수의 개수
    D[i][1] = D[i - 1][0]  # i의 길이에서 끝이 1로 끝나는 이친수의 개수

print(D[N][0] + D[N][1])
