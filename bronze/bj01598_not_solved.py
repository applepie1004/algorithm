a, b = map(int, input().split(" "))

""" 
문제 : https://www.acmicpc.net/problem/1598
풀이 : https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj1598/
간단한 문제입니다.
우선, 원점을 0으로 생각하기 위해 입력받은 값에서 각 1을 빼줍니다.
그후, 가로 좌표는 4로 나눈 몫으로, 세로 좌표는 4로 나눈 나머지로 각각 구하여 계산하면 끝입니다.
"""
