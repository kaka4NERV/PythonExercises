# 斐波那契数列
def Fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)
a = int(input('输入需输出的裴波那契数列项数'))
for i in range(1, a+1):
    print(Fibo(i), end=',')