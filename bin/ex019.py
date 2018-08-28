# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
ls = []
for n in range(1,1001):
    list2 = []
    for i in range(1, n):
        if n % i == 0:
            list2.append(i)
    if sum(list2) == n:
        ls.append(n)
print(ls)