# 직사각형에서 탈출

x, y, w, h = map(int, input().split(' '))

wx = x if x < w - x else w - x  # if 조건 else C
hy = y if y < h - y else h - y

print(wx if wx < hy else hy)


