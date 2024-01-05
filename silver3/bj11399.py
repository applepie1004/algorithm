N = int(input())
A = list(map(int, input().split()))
S = [0]*N

for i in range(1, N):
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1):  # i-1 부터 0(-1은 포함 안됨)까지 -1씩
        # 현재 범위에서 삽입 위치 찾기
        if A[j] < A[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        # 삽입을 위해 삽입 위치에서 i 까지 데이터를 한 칸씩 밀기
        A[j] = A[j-1]
    A[insert_point] = insert_value  # 삽입 위치에 현재 데이터 삽입하기

S[0] = A[0]
for i in range(1, N):
    S[i] = S[i-1] + A[i]

SUM = 0
for i in range(N):
    SUM += S[i]

print(SUM)
