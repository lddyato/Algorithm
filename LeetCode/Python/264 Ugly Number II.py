# -*- coding: utf-8 -*-

'''
Ugly Number II
==============

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
ugly numbers.

Note that 1 is typically treated as an ugly number.
'''


class Solution(object):
    '''算法思路：

    参考了：http://www.geeksforgeeks.org/ugly-numbers/
    '''
    def nthUglyNumber(self, n):
        dp = [1] * n
        p2 = p3 = p5 = 0

        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)

            if dp[i] == dp[p2] * 2:
                p2 += 1

            if dp[i] == dp[p3] * 3:
                p3 += 1

            if dp[i] == dp[p5] * 5:
                p5 += 1

        return dp[-1]


s = Solution()
print s.nthUglyNumber(10)
