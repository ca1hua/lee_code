# 求根公式的运用
import math

# 输入两个整数a和b
a = int(input())
b = int(input())

# 计算判别式
delta = a * a - 4 * b

# 判别式非负，可能有解
if delta >= 0:
    # 计算两个解
    sqrt_delta = math.sqrt(delta)

    # 判断是否是整数
    if sqrt_delta.is_integer():
        # x的两个解
        x1 = (a + sqrt_delta) / 2
        x2 = (a - sqrt_delta) / 2

        # 如果解是整数
        if x1.is_integer() and x2.is_integer():
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
