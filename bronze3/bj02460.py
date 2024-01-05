train = {}
MAX = 0
for idx in range(10):
    leave, take = map(int, input().split(' '))
    train[idx] = {'l': leave, 't': take}
    if idx != 0:
        train[idx]['s'] = train[idx-1]['s'] + take - leave
    else:
        train[idx]['s'] = take

    if MAX < train[idx]['s']:
        MAX = train[idx]['s']

print(MAX)
