# coding=utf-8

# 输入数字字符串，并转换为数值列表
a = input()
num1 = eval(a)
numbers = list(num1)

# 对数值列表numbers实现从小到大排序
numbers.sort()

# 输出排序后的列表
print(numbers)
