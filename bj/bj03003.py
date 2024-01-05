# a = [1, 1, 2, 2, 2, 8]
#
# b = list(map(int, input().split(" ")))
#
# result = ""
# for i in range(len(b)):
#     result += str(a[i] - b[i]) + ' '
#
# print(result.strip())


n = 822211
for i in input().split():
    print(n % 10 - int(i))
    n //= 10
