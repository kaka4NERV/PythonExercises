# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
s = input('输入加数a和相加次数n，以逗号分隔：')
a = int(s.split(',')[0])
n = int(s.split(',')[1])
sum = 0
for i in range(n):
    sum += int(f'{a}' * (i+1))
print(sum)