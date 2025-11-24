import collections
def Func():
    pairs = []
    n = int(input())
    od = collections.OrderedDict()
    for s in range(n):
        k = input()
    # ********** Begin ********** #
        pairs.append((k,s))
    od = collections.OrderedDict(sorted(pairs, key=lambda s: s[0]))  # 按数据中key值的大小排序
    # ********** End ********** #
    print(od)