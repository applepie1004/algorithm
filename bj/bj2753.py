# gs = list(input())
#
# if len(gs) == 1:
#     print("0.0")
# else:
#     score = 0.0
#     score += 0.3 if gs[1] == "+" else (0 if gs[1] == "0" else -0.3)
#
#     score += 4 if gs[0] == "A" else (3 if gs[0] == "B" else (2 if gs[0] == "C" else 1))
#     print(score)
#

a,b,*c=input()+'0' # *c,+0은 값으로 F가 들어올 때를 위해 추가 코드
print('FDCBA'.find(a)+.3*'0+'.find(b))