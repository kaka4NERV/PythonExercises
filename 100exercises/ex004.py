# 输入某年某月某日，判断这一天是这一年的第几天？
ls = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]
inputdate = input('按yyyymmdd格式输入日期')
year = int(inputdate[0:4].lstrip('0'))
month = int(inputdate[4:6].lstrip('0'))
days = int(inputdate[6:8].lstrip('0'))
days_counter = 0
if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month > 2:
    days_counter = sum(ls[:month-1]) + days + 1
else:
    days_counter = sum(ls[:month - 1]) + days
print(days_counter)