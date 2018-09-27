# 打印出如下图案（菱形）:
'''   *
     ***
    *****
   *******
    *****
     ***
      *
'''
n = int(input('enter a number:'))
for  i  in range(1,n+1,2):
    k = (n-i)//2
    print( ' '* k , '*' * i)

for  p in range(n-2,0,-2):
    o = (n-p)//2
    print(' '*o, '*'*p)