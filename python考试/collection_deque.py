import collections
def Func():
    d = collections.deque()
    n = int(input())
    # ********** Begin ********** #
    for i in range(n):
        if i % 2 == 0:
            d.append(i)
        else:
            d.appendleft(i)

    # ********** End ********** #
    print(d)

'''
range(5) 生成 [0, 1, 2, 3, 4]

range(2, 6) 生成 [2, 3, 4, 5]

range(0, 10, 2) 生成 [0, 2, 4, 6, 8]

range(10, 0, -2) 生成 [10, 8, 6, 4, 2]
'''