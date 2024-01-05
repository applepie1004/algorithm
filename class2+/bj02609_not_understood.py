a,b = map(int,input().split())


# 최대공약수
# a & b의 최대 공약수는 b & a를 b로 나눈 나머지의 최대 공약수
def gcd(a1, b1):
    while b1 > 0:
        a1, b1 = b1, a1 % b1
        print('gcd1', a1, b1)
    return a1


def gcd2(a1, b1):
    while b1 > 0:
        a1 = b1
        b1 = a1 % b1
        print('gcd2', a1, b1)
    return a1


# 최소공배수
# a와 b의 곱을 a와 b의 최대 공약수로 나눈 값
def lcm(a1, b1):
    return a1 * b1 // gcd(a1, b1)


gcd(a, b)
gcd2(a, b)

# print(gcd(a, b))
# print(gcd2(a, b))
# print(lcm(a, b))
