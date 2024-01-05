n = int(input())
na = list(map(int, input().split(" ")))
m = int(input())
ma = list(map(int, input().split(" ")))

na.sort()


# 이분탐색 : 중간값 부터 찾을 수를 검색 하는 것,
# 만약 원하는 값이 아니면, 앞뒤로 절반을 잘라 또 다시 중간 값을 확인
for i in ma:
    lt, rt = 0, n-1
    isExist = False
    
    print(i)
