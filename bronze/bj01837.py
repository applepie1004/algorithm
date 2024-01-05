import sys

a, b = map(int, sys.stdin.readline().split(' '))

value1 = 0
value2 = 0
for i in range(2, b+1):
    if a % i == 0:
        value1 = i
        value2 = a // i
        break

if value1 == 0 and value2 == 0:
    print('GOOD')
elif value1 < b:
    print('BAD', value1)
elif value2 < b:
    print('BAD', value2)
else:
    print('GOOD')
