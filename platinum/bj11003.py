from collections import deque

N, L = map(int, input().split())
now = list(map(int, input().split()))

myDeque = deque()

for i in range(N):
    # myDeque가 있거나, myDeque의 마지막인덱스가 now값보다 크다면 deque에서 삭제
    while myDeque and myDeque[-1][0] > now[i]:
        myDeque.pop()
    myDeque.append((now[i], i))

    if myDeque[0][1] <= i - L:
        myDeque.popleft()

    print(myDeque[0][0], end=" ")
