nums = list(range(1, 31))

while len(nums) > 2: nums.pop(nums.index(int(input())))

for j in nums: print(j)
