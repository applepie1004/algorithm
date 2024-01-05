for i in range(0, int(input())):
    t = input().split(" ")
    txt = ""
    for j in t[1]:
        for k in range(0, int(t[0])):
            txt = txt + j
    print(txt)
