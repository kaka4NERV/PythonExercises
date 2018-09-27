# 求1+2!+3!+...+20!的和。
for i in range(1,21):
    count = 1
    for j in range(i,0,-1):
        count *= j
    sum = 0
    sum += count
print(sum)