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


class Solution:
    '''算法思路：

    https://leetcode.com/discuss/52905/my-16ms-c-dp-solution-with-short-explanation
    '''
    def nthUglyNumber(self, n):
        if n <= 1:
            return max(0, n)

        k = [0] * n
        k[0] = 1

        t2 = t3 = t5 = 0

        for i in xrange(1, n):
            k[i] = min(k[t2]*2, k[t3]*3, k[t5]*5)

            if k[i] == k[t2]*2:
                t2 += 1

            if k[i] == k[t3]*3:
                t3 += 1

            if k[i] == k[t5]*5:
                t5 += 1

        return k[n-1]


s = Solution()
print s.nthUglyNumber(10)
