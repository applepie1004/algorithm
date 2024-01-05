checkArr = [0] * 4
myArr = [0] * 4  #
checkSecret = 0


def myadd(c):  # 새로 들어온 문자를 처리하는 함수
    global checkArr, myArr, checkSecret
    if c == 'A':
        myArr[0] += 1
        if myArr[0] == checkArr[0]:
            checkSecret += 1
    elif c == 'C':
        myArr[1] += 1
        if myArr[1] == checkArr[1]:
            checkSecret += 1
    elif c == 'G':
        myArr[2] += 1
        if myArr[2] == checkArr[2]:
            checkSecret += 1
    elif c == 'T':
        myArr[3] += 1
        if myArr[3] == checkArr[3]:
            checkSecret += 1

    print(checkArr, myArr, checkSecret)


def myremove(c):  # 제거되는 문자를 처리하는 함수
    global checkArr, myArr, checkSecret
    if c == 'A':
        if myArr[0] == checkArr[0]:
            checkSecret -= 1
        myArr[0] -= 1
    elif c == 'C':
        if myArr[1] == checkArr[1]:
            checkSecret -= 1
        myArr[1] -= 1
    elif c == 'G':
        if myArr[2] == checkArr[2]:
            checkSecret -= 1
        myArr[2] -= 1
    elif c == 'T':
        if myArr[3] == checkArr[3]:
            checkSecret -= 1
        myArr[3] -= 1
    # print(checkArr, myArr, checkSecret)


S, P = map(int, input().split(' '))
A = input()
checkArr = list(map(int, input().split(' ')))  # A, C, G, T
result = 0
for i in range(4):
    if checkArr[i] == 0:
        checkSecret += 1

for i in range(P):   # 초기 P 부분 문자열 처리 부분
    myadd(A[i])

if checkSecret == 4:  # 4자릿수와 관련된 크기가 모두 충족될 때 유효한 비밀번호
    result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        result += 1
