class Solution():
    def solve(self, l, r):
        '''
        :type l, r: int
        :rtype : list
        '''
        # 请在此添加代码，实现求得[l, r]范围内的所有素数，并将其返回
        # ********** Begin *********#
        result = []
        for num in range(l, r + 1):
            if num < 2:
                continue

            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                result.append(num)

        return result
        # ********** End *********#