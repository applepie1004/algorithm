"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""
import sys

na = []
for i in range(0, num := int(input())):
    na.append(int(sys.stdin.readline()))


for i in range(len(na)):
    for j in range(i+1, len(na)):
        if na[i] > na[j]:
            na[i], na[j] = na[j], na[i]

for i in na:
    print(i)


