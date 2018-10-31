# 输入三个整数x,y,z，请把这三个数由小到大输出。
# numbs = input('输入三个整数并以空格分隔')
# numbslist = numbs.split(' ')
# print(sorted(numbslist))
input1 = int(input('输入第一个整数'))
input2 = int(input('输入第二个整数'))
input3 = int(input('输入第三个整数'))
x = y = z = input1
ls = [input1, input2, input3]
for i in ls:
    if i > x:
        x = i
    elif i < z:
        z = i
    else:
        y = i
print(f'{z}\n{y}\n{x}')