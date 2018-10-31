# 使用规则点阵求圆的面积
r = int(input('请输入规则点阵边长:'))//2
counts = 0
area = 0
for a in range(-r, r):
    for b in range(-r,r):
        if a**2 + b**2 <= 500**2:
            counts += 1
pi = counts/(r**2)
print(pi)
