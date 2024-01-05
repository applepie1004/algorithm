"""
n번째 삼각수, T(n)은 1부터 n까지의 합이다. T(n) = 1 + ... + n. 이것은 삼각형 모양으로 표현할 수 있다. 아래 그림은 T(4)를 나타낸 것이다.
*
**
***
****
다음과 같은 식을 통해 가중치를 부여한 삼각수의 합을 구할 수 있다.

W(n) = Sum[k=1..n; k*T(k+1)]
해석을 해보자.

T(n) = 1 + 2 + ... + n

n이 주어졌을 때, W(n)을 구하는 프로그램을 작성하시오.
"""


def T(n):
    _sum = 0
    for i in range(1, n+1):
        _sum += i
    return _sum


def W(n):
    _sum = 0
    for i in range(1, n+1):
        _sum += i * T(i+1)
    return _sum


for _ in range(int(input())):
    print(W(int(input())))
