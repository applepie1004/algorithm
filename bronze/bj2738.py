sn, sm = map(int, input().split(" "))

arr1 = [[0 for col in range(sm)] for row in range(sn)]
arr2 = [[0 for col in range(sm)] for row in range(sn)]

for i in range(sn):
    arr1[i] = list(map(int, input().split(" ")))

for i in range(sn):
    arr2[i] = list(map(int, input().split(" ")))

for i in range(sn):
    result = ""
    for j in range(sm):
        result += str(arr1[i][j] + arr2[i][j])
        if j < sm-1:
            result += " "
        if j == sm-1:
            print(result)
