# -*- coding: utf-8 -*-

'''
Super Ugly Number
=================

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the
given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16,
19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given
primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000.
'''


class Solution(object):
    '''算法思路：

    同 264 Ugly Number II
    '''
    def nthSuperUglyNumber(self, n, primes):
        k = len(primes)
        dp, p = [1] * n, [0] * k

        for i in range(1, n):
            candidates = [dp[p[j]] * primes[j] for j in range(k)]
            dp[i] = min(candidates)

            for j in range(k):
                if dp[i] == candidates[j]:
                    p[j] += 1

        return dp[-1]


s = Solution()
print s.nthSuperUglyNumber(12, [2, 7, 13, 19])

