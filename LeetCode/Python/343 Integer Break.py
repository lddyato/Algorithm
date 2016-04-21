# -*- coding: utf-8 -*-

'''
Given a positive integer n, break it into the sum of at least two positive
integers and maximize the product of those integers. Return the maximum product
you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36
(10 = 3 + 3 + 4).

Note: you may assume that n is not less than 2.
'''


class Solution(object):
    def integerBreak(self, n):
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(
                    dp[i],
                    dp[j] * dp[i - j],
                    dp[j] * (i - j),
                    j * dp[i - j],
                    j * (i - j)
                )
        return dp[-1]


s = Solution()
print s.integerBreak(3)
