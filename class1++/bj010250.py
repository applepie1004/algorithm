for i in range(int(input())):
    h, w, n = map(int, input().split(" "))
    priority = []

    for j in range(w):
        for k in range(h):
            priority.append(str(k+1)+str(j+1).rjust(2, '0'))

    print(priority[n-1])
