# coding=utf-8

# 输入一个正整数

x = int(input())
n = x
# 请在此添加代码，将输入的一个正整数分解质因数
result = []

# 从2开始枚举到sqrt(x)，尝试将x除以当前数
i = 2
while i * i <= x:
    while x % i == 0:  # 如果i是x的因数，则记录下来，并继续除以i
        result.append(i)
        x //= i
    i += 1

# 如果x大于1，则x本身是一个质数，加入结果
if x > 1:
    result.append(x)

# 输出结果，利用map()函数将结果按照规定字符串格式输出
print(f'{n} = {"*".join(map(str, result))}')
