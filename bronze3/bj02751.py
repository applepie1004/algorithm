"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""
import sys

na = []
for _ in range(0, int(input())):
    na.append(int(sys.stdin.readline()))

na.sort()

for i in na:
    print(i)
# f = open("D:/개인/알고리즘/1000000.txt", "w+")
# li = list(range(1, int(input())+1))
# li.reverse()
#
# for i in li:
#     f.write(str(i)+"\n")
# f.close()
