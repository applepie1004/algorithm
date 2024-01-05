for _ in range(int(input())):
    blank = input()
    li = []
    s = int(input())
    for __ in range(s):
        li.append(int(input()))
    print("NO" if sum(li) % s else "YES")
