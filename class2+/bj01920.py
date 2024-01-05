n = int(input())
N = sorted([int(i) for i in input().split(" ")])

m = int(input())
M = [int(i) for i in input().split(" ")]

for i in M:
    st, ed = 0, n-1
    isExist = False

    # 이분탐색
    while st <= ed:
        mid = (st + ed) // 2  # 정수로 반 쪼개기
        if i == N[mid]:
            isExist = True
            print(1)
            break
        elif i > N[mid]:  # i의 값이 N[mid]보다 클 때
            st = mid + 1  # st의 값을 mid + 1로 변경한다.
        else:
            ed = mid - 1

    if not isExist:
        print(0)
