
n = int(input())

# 请在此添加代码，对输入的正整数n进行阶乘运算，并输出计算结果。
########## Begin ##########
def Factorial(n):
    if n == 0 or n == 1:  # 0! = 1 和 1! = 1
        return 1
    else:
        return n * Factorial(n-1)

# 输出计算结果
print(Factorial(n))


########## End ##########

