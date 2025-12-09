class Solution():
    def get_lcm(self, x):
        #请在此添加代码，实现求出给定的所有正整数的最小公倍数，并将其返回
        #********** Begin *********#
        def gcd(x, y):
            return x if y == 0 else gcd(y, x%y)
        def lcm(x, y):
            return x // gcd(x, y) * y
        ans = x[0]
        for index in range(len(x)-1):
            x[index+1] = lcm(x[index], x[index+1])
            ans = max(ans, x[index+1])
        return ans
        #********** End **********#
        pass