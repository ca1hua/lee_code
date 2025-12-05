# coding=utf-8
from math import pi as PI

# 定义计算圆面积的函数
def calculate_area(radius):
    return PI * radius ** 2

# 获取用户输入的半径
n = int(input())

# 调用函数计算圆的面积
area = calculate_area(n)

# 输出结果，保留两位小数
print(f"{area:.2f}")