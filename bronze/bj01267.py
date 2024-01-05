call = int(input())
callTimes = list(map(int, input().split()))

y = 0
m = 0
for i in callTimes:
    y += i // 30 + 1
    m += i // 60 + 1

yPrice, mPrice = y * 10, m * 15
if yPrice == mPrice:
    print('Y M', yPrice)
elif yPrice > mPrice:
    print('M', mPrice)
elif yPrice < mPrice:
    print('Y', yPrice)

