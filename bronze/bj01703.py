while (nums := input()) != '0':
    branchorama = list(map(int, nums.split(' ')))
    leaf = 1
    for i in range(branchorama[0]):  # 나이(n)만큼 반복
        leaf = leaf * branchorama[2*i + 1] - branchorama[2*i + 2]
    print(leaf)
