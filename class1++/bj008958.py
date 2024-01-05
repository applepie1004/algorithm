for i in range(int(input())):
    ol = input().split("X")
    total = 0
    for j in ol:
        if len(j) > 0:
            for k in range(len(j)):
                total = total + (k + 1)
    print(total)