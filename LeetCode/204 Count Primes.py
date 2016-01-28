# -*- coding: utf-8 -*-

'''
Count Primes
============

Description:

Count the number of prime numbers less than a non-negative number, n.
'''


class Solution(object):
    '''算法思想：

    从奇数 3 从小到大遍历数组，将当前数的倍数在数组中标记为 None，一直这样下去，最后
    数组中不为 None 的个数即为所求

    利用的原理是：素数的倍数必不是素数
    '''
    def countPrimes(self, n):
        if n < 3:
            return 0

        array = range(3, n, 2)

        sqrt = int(pow(len(array), 0.5))
        if sqrt * sqrt != len(array):
            sqrt += 1

        for i in xrange(sqrt):
            num = array[i]
            if not num:
                continue

            times = num
            while times * num < n:
                array[(times * num - 3) / 2] = None
                times += 2

        return len(filter(None, array)) + 1


s = Solution()
print s.countPrimes(50)
