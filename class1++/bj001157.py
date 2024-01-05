tt = list(input().upper())
counter = {}
for t in tt:
    if t in counter:
        counter[t] += 1
    else:
        counter[t] = 1

mm, mt = 0, ""
ct = list(counter.keys())
cv = list(counter.values())
for i in range(0, len(cv)):
    if mm < cv[i]:
        mm = cv[i]
        mt = ct[i]
    elif mm == cv[i]:
        mm = cv[i]
        mt = "?"

print(mt)