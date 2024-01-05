""" input
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
"""
import sys


input = sys.stdin.readline


li = [0] + [1, 2, 3, 4, 5]
print(li)

li2 = [0] * 5
print(li2)

n, m = map(int, input().split(' '))
A = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

print(A)

D = [[0 * (n + 1)] * (n + 1)] * (n + 1)

print(D)
