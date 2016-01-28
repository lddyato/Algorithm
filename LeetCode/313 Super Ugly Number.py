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

    标记 t[i] 表示 primes[i] 出现的次数，每次比较是 dp[t[i]] * primes[i] 之间的比较
    '''
    def nthSuperUglyNumber(self, n, primes):
        dp, t = [0] * n, [0] * len(primes)

        dp[0] = 1
        for i in xrange(1, n):
            dp[i] = min([dp[t[j]] * primes[j] for j in xrange(len(primes))])

            for j in xrange(len(primes)):
                t[j] += dp[i] == dp[t[j]] * primes[j]

        return dp[n - 1]


s = Solution()
print s.nthSuperUglyNumber(12, [2, 7, 13, 19])

