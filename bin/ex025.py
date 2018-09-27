# 求1+2!+3!+...+20!的和。
sum = 0
for i in range(1,21):
    count = 1
    for j in range(i,0,-1):
        count *= j
    sum += count
print(sum)

n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    print(t)
    s += t
print(s)