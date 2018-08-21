#  8. 输出 9*9 乘法口诀表。
n = 2
for i in range(1, 10):
    for j in range(1, n):
        print(f'{i} * {j} = {i * j}', end='  ')
    else:
        n += 1
        print('')