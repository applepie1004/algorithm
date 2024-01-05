import collections

dices = []
for idx in range(int(input())):
    total = 0
    li = list(map(int, input().split(' ')))

    dice = dict(collections.Counter(li))

    _max = max(list(dice.keys()))

    if len(dice) == 1:
        total = 10000 + _max * 1000

    elif len(dice) == 2:
        for i in dice:
            if dice[i] == 2:
                total = 1000 + i * 100
                break

    elif len(dice) == 3:
        total = _max * 100

    dices.append(total)

print(max(dices))
