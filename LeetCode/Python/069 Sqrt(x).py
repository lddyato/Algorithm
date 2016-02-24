# -*- coding: utf-8 -*-

'''
Sqrt(x)
=======

Implement int sqrt(int x).

Compute and return the square root of x.
'''


class Solution(object):
    '''算法思想：

    二分逼近

    需要注意的有以下几点：
    - 找到结果时，diff > 0
    '''
    def mySqrt(self, x):
        low, high = 0, x
        while 1:
            mid = (low + high) / 2.0
            diff = mid ** 2 - x

            if diff >= 0 and diff < 1e-6:
                return int(mid)

            if diff < 0:
                low = mid + 1
            else:
                high = mid - 1


class Solution(object):
    '''算法思路：

    二分逼近，由于要返回的是整数，所以找到最后一个满足 r^2 <= x 的整数即可
    '''
    def mySqrt(self, x):
        low, high = 0, x
        while low <= high:
            mid = low + high >> 1
            diff = mid ** 2 - x

            if diff <= 0:
                low = mid + 1
            else:
                high = mid - 1
        return low - 1


s = Solution()
print s.mySqrt(25)
