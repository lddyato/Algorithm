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
    - count 的加入是为了避免由于 diff 的精度不够而陷入死循环
    - 找到结果时，diff > 0
    '''
    def mySqrt(self, x):
        low, high, e, count = 0, x, 1e-8, 0
        while count <= 100:
            mid = (low + high) / 2.0

            diff = mid ** 2 - x
            if abs(diff) <= e and diff > 0:
                break

            if diff > 0:
                high = mid
            else:
                low = mid

            count += 1

        return int(mid)


s = Solution()
print s.mySqrt(25)
