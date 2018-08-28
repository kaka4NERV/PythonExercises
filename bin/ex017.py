# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import string
def count(InputStr):
    char_counter = 0
    space_counter = 0
    number_counter = 0
    other_counter = 0
    for i in InputStr:
        if i.isalpha():
            char_counter += 1
        elif i.isdigit():
            number_counter += 1
        elif i.isspace():
            space_counter += 1
        else:
            other_counter += 1
    print(char_counter, space_counter, number_counter, other_counter)
i = input('请输入任意字符串：')
count(i)

s = input('请输入一个字符串:')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))