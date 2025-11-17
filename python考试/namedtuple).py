import collections

def CreatePoint():
    # ********** Begin ********** #
    Point = collections.namedtuple("Point","x,y")
    return Point(x = 0,y = 0)
    # ********** End ********** #

def IncX(p):
    # ********** Begin ********** #
    p = p._replace(x = p.x + 1)
    return p

    # ********** End ********** #

def IncY(p):
    # ********** Begin ********** #
    p = p._replace(y = p.y + 1)
    return p

    # ********** End ********** #

def PrintPoint(p):
    print("当前位置:x = %d,y = %d" % p)