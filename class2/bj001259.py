while (b := input()) != '0':
    if b == b[::-1]:
        print('yes')
    else:
        print('no')
