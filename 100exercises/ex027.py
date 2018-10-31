# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
s = input('>')
l = len(s)
def output(l, s):
    if l == 0:
        return
    print(s[l-1])
    output(l-1, s)
output(l, s)