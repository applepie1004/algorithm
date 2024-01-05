A = list(input())

for i in range(len(A)):
    MAX = i
    for j in range(i+1, len(A)):
        if A[j] > A[MAX]:
            MAX = j
    if A[i] < A[MAX]:
        A[i], A[MAX] = A[MAX], A[i]

print(''.join(A))
