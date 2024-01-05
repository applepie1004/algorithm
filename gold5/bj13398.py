N = int(input())
A = list(map(int, input().split(" ")))

L = A.copy()
R = A.copy()

# 오른쪽 부터 구간합
for i in range(1, N):
    L[i] = max(A[i], L[i-1] + A[i])

# 왼쪽(역순)부터 구간합
for i in range(N-2, 1, -1):
    R[i] = max(A[i], R[i+1] + A[i])

# L[i-1] + R[i + 1] 2개의 구간 합 배열을 더하면 i번째 값을 제거한 효과를 얻음
# for i in range(1, N-1):
#     temp = L[i-1] + R[i+1]
#     result = max(result, temp)


result = max(L)  # 기존 구간합 배열의 max값
result2 = -1001  # 수를 제거하거나 제거하지 않았을 경우의 max값

for i in range(1, N-1):
    result2 = max(result2, L[i-1] + R[i+1])

print(max(result, result2))