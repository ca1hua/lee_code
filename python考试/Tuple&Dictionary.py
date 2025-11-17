''''# coding=utf-8

# 元组的元素不能修改
menu_list = []
while True:
    try:
        food = input()
        menu_list.append(food)
    except:
        break

# 请在此添加代码，对menu_list进行元组转换以及元组计算等操作，并打印输出元组及元组最大的元素
###### Begin ######

menu_tuple = tuple(menu_list)
print(menu_tuple[:])
print(max(menu_tuple))

#######  End #######'''

"""

# coding=utf-8
# 创建并初始化munu_dict字典
menu_dict = {}
while True:
    try:
        food = input()
        price = int(input())
        menu_dict[food]= price
    except:
        break
# 请在此添加代码，实现对menu_dict的遍历操作并打印输出键与值
########## Begin ##########

for key in menu_dict.keys():
    print(key)

for value1 in menu_dict.values():
    print(value1)


########## End ##########
print(key)"""

# coding=utf-8

# 创建并初始化menu_dict字典
menu_dict = {}
while True:
    try:
        food = input()
        price = int(input())
        menu_dict[food] = price
    except:
        break

# 请在此添加代码，实现对menu_dict的添加、查找、修改等操作，并打印输出相应的值
########## Begin ##########
menu_dict['lamb'] = 50

########## End ##########
