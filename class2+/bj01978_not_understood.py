N = int(input())
A = list(map(int, input().split(" ")))

result = 0

for a in A:
    isExist = False
    if a > 1:
        for i in range(2, a):
            if a % i == 0:  # 나눠지는게 있다면
                isExist = True  # True 로 바꾸고
                break  # 그만 돌리고
        if not isExist:
            result += 1

print(result)
