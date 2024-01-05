a, b, c = int(input()), int(input()), int(input())
cal = a * b * c

counter = [0 for i in range(10)]
for t in str(cal):
    counter[int(t)] += 1

[print(k) for k in counter]
