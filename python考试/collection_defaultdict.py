import collections
def GetIntDefaultDict():
# 返回一个空的int类型的默认字典
# ********** Begin ********** #
    return  collections.defaultdict(int)

# ********** End ********** #

def GetListDefaultDict():
# 返回一个空的list类型的默认字典
# ********** Begin ********** #
    return  collections.defaultdict(list)


# ********** End ********** #

def GetTupleDefaultDict():
# 返回一个空的tuple类型的默认字典
# ********** Begin ********** #
    return collections.defaultdict(tuple)

# ********** End ********** #
def GetStrDefaultDict():
# 返回一个空的str类型的默认字典
# ********** Begin ********** #
    return collections.defaultdict(str)

# ********** End ********** #
