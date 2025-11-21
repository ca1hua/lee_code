import collections
def Func():
    c = collections.Counter()
    for i in range(6):
        data = input()
        # ********** Begin ********** #
        if i % 2 == 0:                     #注意冒号
                    c.update(data)
        else:
                    c.subtract(data)

        # ********** End ********** #
    print(c.most_common(1))

Func()