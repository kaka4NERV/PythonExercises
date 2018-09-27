# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
a = 2
b = 1
count = 0

for i in range(1,21):
    count += a/b
    t = a
    a = b + t
    b= t

print(count)
