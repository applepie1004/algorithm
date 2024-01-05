mx, mn = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
mns = list()

for i in nums:
    if i < mn:
        mns.append(i)

print(" ".join(map(str, mns)))
