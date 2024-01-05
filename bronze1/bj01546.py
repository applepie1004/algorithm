n = int(input())

nums = [int(i) for i in input().split(" ")]

s = 0
m = 0
for i in nums:
    s += i
    if m < i:
        m = i

print(s*100/m/n)