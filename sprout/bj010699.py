import datetime

d = datetime.datetime.now()
print(f'{d.year}-{str(d.month).rjust(2, "0")}-{str(d.day).rjust(2, "0")}')
