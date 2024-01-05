for idx in range(3):
    li = list(map(int, input().split(" ")))
    cnt = li.count(1)

    if cnt == 1:
        print("C")
    elif cnt == 2:
        print("B")
    elif cnt == 3:
        print("A")
    elif cnt == 4:
        print("E")
    elif cnt == 0:
        print("D")
