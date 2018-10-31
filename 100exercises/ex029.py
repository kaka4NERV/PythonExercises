# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
s = input('>')
l = len(s)
print(f'输入的是{l}位数')
s = list(s)
s.reverse()
print(s)