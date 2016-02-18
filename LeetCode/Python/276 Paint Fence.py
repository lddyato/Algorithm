# -*- coding: utf-8 -*-

'''
Paint Fence
===========

There is a fence with n posts, each post can be painted with one of the k
colors.

You have to paint all the posts such that no more than two adjacent fence posts
have the same color.

Return the total number of ways you can paint the fence.
'''


class Solution(object):
    '''算法思路：

    fence 不是环状的
    '''
    def numWays(self, n, k):
        if n <= 0 or k <= 0:
            return 0

        dp = [0] * n

        dp[0] = k
        if n > 1:
            dp[1] = k * k

        for i in xrange(2, n):
            dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)

        return dp[n - 1]


s = Solution()
print s.numWays(3, 3)
