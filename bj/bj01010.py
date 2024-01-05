def factorial(a):
    num = 1
    for i in range(1, a+1):
        num *= i
    return num


for _ in range(0, int(input())):
    n, m = map(int, input().split(' '))
    # 공식 : mCn = m! // (m-n)!n!
    result = factorial(m) // (factorial(m-n)*factorial(n))
    print(result)
