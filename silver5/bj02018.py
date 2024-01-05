N = int(input())

cnt, start_idx, end_idx, SUM = 1, 1, 1, 1
while end_idx < N:
    if SUM > N:
        SUM -= start_idx
        start_idx += 1
    elif SUM < N:
        end_idx += 1
        SUM += end_idx
    else:
        cnt += 1
        end_idx += 1
        SUM += end_idx
print(cnt)