# coding=utf-8

# 输入一个整数n
n = int(input())


# 请在此添加代码，对输入的整数进行判断，如果是素数则输出为True，不是素数则输出为False
########## Begin ##########
def prime(n):
    if n == 1:
        return 'False'
    for i in range(2,n):
        if (n % i == 0):
            return 'False'
    return 'True'


########## End ##########
print(prime(n))

