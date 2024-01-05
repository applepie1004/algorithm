"""
5명의 요원 중 FBI 요원을 찾는 프로그램을 작성하시오.
FBI요원은 요원의 첩보원명에 FBI가 들어있다.
"""
li = []
for i in range(5):
    if input().find("FBI") > -1:
        li.append(str(i+1))

if len(li) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(li))
