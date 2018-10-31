# 使用蒙特卡洛方法求Pi
import random
turns = int(input('请输入试验点数：')) # 实验次数
counts = 0 # 落在半径为1的圆内的点数
area = 0 # 四分之一圆的面积
i = 0 # 累加数
while i < turns:
    a = random.random()
    b = random.random()
    if a**2 + b**2 <= 1: # 判断点是否在圆内
        counts += 1
    i += 1
else:
    area = counts / turns # 边长为1的正方形乘以落在圆内的比例求面积
pi = 4 * area
print(f'通过{turns}试验点数求出的pi为{pi}')

