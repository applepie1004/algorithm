"""
- 투 포인터
앞에서부터 탐색하되, end index를 늘려나가며 sum을 하다가
해당 값 보다 크면 start index 를 늘린다.
해당 값이 되면 count를 올리고 end index를 넘김
"""
N = int(input())
li = [int(i) for i in range(1, N + 1)]

count = 1  # 연속으로 합이 N일 경우 ++, N값 혼자 해당 값인 경우
start_index = 1
end_index = 1
_sum = 1  # 연속으로 합이 N일 경우를 확인

while end_index != N:
    print(start_index, end_index)
    if _sum == N:
        count += 1
        end_index += 1
        _sum += end_index
    elif _sum < N:
        end_index += 1
        _sum += start_index
    else:  # _sum > N
        _sum -= start_index
        start_index += 1

print(count)
