# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
def rate(n):
    if n >= 90:
        return 'A'
    elif n >=60:
        return 'B'
    else:
        return 'C'
n = int(input('请输入分数：'))
print(rate(n))