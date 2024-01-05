n = int(input())

nums = [int(i) for i in input().split(" ")]
print(sum(nums)*100 / max(nums) / n)
