import datetime

h, m = map(int, input().split(' '))
time = datetime.datetime(2018, 4, 1, h, m)
time = time + datetime.timedelta(minutes=int(input()))

print(time.hour, time.minute)

