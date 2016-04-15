# -*- coding: utf-8 -*-

'''
Perfect Squares
===============

Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
return 2 because 13 = 4 + 9.
'''


class Solution(object):
    '''算法思路：

    设 f(n) 为最少个数，那么

    f(n) = min(f(n-1), f(n-4), f(n-9)..., f(sqrt(n) * sqrt(n))) + 1

    结果：maximum recursion depth exceeded
    '''
    def cache(f):
        def method(obj, n):
            if obj.record[n] == -1:
                obj.record[n] = f(obj, n)
            return obj.record[n]
        return method

    @cache
    def search(self, n):
        if n < 4:
            return n

        return min(self.search(n - i * i) + 1
                   for i in xrange(1, int(pow(n, 0.5)) + 1))

    def numSquares(self, n):
        self.record = [-1] * (n + 1)
        return self.search(n)


class Solution(object):
    '''算法思路：

    动态规划

    结果：TLE
    '''
    def numSquares(self, n):
        dp = [0] * (n + 1)

        dp[1] = 1
        for i in xrange(2, n + 1):
            dp[i] = min(
                dp[i - j**2] for j in xrange(1, int(i**0.5) + 1)) + 1

        return dp[n]


class Solution(object):
    '''算法思路：

    同上，不过把 dp 是 static 的，即是 class 的属性，这样做的原因是，对于 leetcode
    的各个 test case 不用每次都生成 numSquares(n) 的值

    该题和《322 Coin Change》类似

    结果：AC
    '''

    dp = [0]
    def numSquares(self, n):
        MAX = float('inf')
        candidates = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]

        for i in range(len(self.dp), n + 1):
            self.dp.append(min(
                self.dp[i - square] if i >= square else MAX
                for square in candidates
            ) + 1)

        return self.dp[n]


s = Solution()
print s.numSquares(4)
