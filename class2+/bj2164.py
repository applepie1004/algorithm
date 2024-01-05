from collections import deque

na = deque(range(1, int(input())+1))
while len(na) != 1:
    na.popleft()
    na.rotate(-1)

print(na[0])
