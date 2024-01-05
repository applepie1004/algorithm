x = int(input())
result = 0

for i in format(x, 'b'):
    if i == '1':
        result += 1

print(result)
