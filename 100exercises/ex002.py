# 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
bonus = 0
i = float(input('输入当月利润(单位为万）'))
if i > 100:
    bonus = (i - 100) * 0.01 + 40 * 0.015 + 20 * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.1
elif i > 60:
    bonus = (i - 60) * 0.015 + 20 * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.1
elif i > 40:
    bonus = (i - 40) * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.1
elif i > 20:
    bonus = (i - 20) * 0.05 + 10 * 0.075 + 10 * 0.1
elif i > 10:
    bonus = (i - 10) * 0.075 + 10 * 0.1
else:
    bonus = i * 0.1
print(f'奖金总数为{bonus}万')
