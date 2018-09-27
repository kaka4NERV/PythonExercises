# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
s = input('请输入数字：')
l = len(s)
for i in range(0, (l//2)+1):
    if s[i] != s[-(1+i)]:
        print('输入的不是回文数')
        break
else:
    print('输入的是回文数')
