# 打印出如下图案（菱形）:
'''   *
     ***
    *****
   *******
    *****
     ***
      *
'''
def pic(lines):
    middle, lines = int(lines / 2), int(lines / 2) * 2 + 1
    for i in range(1, lines + 1):
        empty = abs(i - middle - 1)
        print(' ' * empty, '*' * (2 * (middle - empty) + 1))
line = 7 # 设置输出行数
pic(7)