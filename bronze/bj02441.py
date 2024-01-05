n = int(input())

blank = ''
star = '*' * n
for i in range(n):
    print(f'{blank}{star[i:n]}')
    blank += ' '
