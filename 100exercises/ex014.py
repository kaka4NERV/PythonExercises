# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
def cal(n):
    ls = []
    N = n
    if n <= 2:
        return print(f"{N}=1 * {N}")
    else:
        while n != 1:
            for i in range(2, n+1):
                if n % i == 0:
                    ls.append(str(i))
                    n //= i
                    break
        print(f"{N}={'*'.join(ls)}")
n = int(input("请输入正整数："))
cal(n)