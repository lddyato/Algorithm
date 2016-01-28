# -*- coding: utf-8 -*-

'''
Maximum Product Subarray
========================

Find the contiguous subarray within an array (containing at least one number)
which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''


class Solution(object):
    '''算法思路：

    计算两两之积

    Time: O(n^2)

    结果：TLE
    '''
    def maxProduct(self, nums):
        n, maximum = len(nums), float('-inf')
        dp = [[1] * n for _ in xrange(n)]

        for i in xrange(n):
            for j in xrange(i, n):
                dp[i][j] = (dp[i][j - 1] if i != j else 1) * nums[j]
                maximum = max(maximum, dp[i][j])

        return maximum


class Solution(object):
    '''算法思路：

    维护两个变量，当前最小连续乘积 和 当前最大连续乘积，并且从最大连续乘积里边选出最大
    的，这样做的原理是，当前最大连续乘积来源有三种，之前最大的乘以当前数，之前最小乘以
    当前数，当前数
    '''
    def maxProduct(self, nums):
        currentMax, currentMin, maximum = 1, 1, float('-inf')
        for num in nums:
            currentMax, currentMin = map(
                lambda f: f(num, currentMax * num, currentMin * num),
                (max, min))
            maximum = max(maximum, currentMax)
        return maximum


s = Solution()
print s.maxProduct([0, 2, -1, -9])
