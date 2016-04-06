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

    动态规划，维护目前最小值和最大值序列
    maxValue[i] 表示前 i 个以第 i 个结尾的最大乘积
    minValue[i] 表示前 i 个以第 i 个结尾的最小乘积

    最大乘积 = max(maxValue[i - 1] * nums[i], minValue[i - 1] * nums[i], nums[i])
    最小乘积 = mix(maxValue[i - 1] * nums[i], minValue[i - 1] * nums[i], nums[i])

    中间过程中比较最大乘积即可

    Time: O(n)
    Space: O(n)
    '''
    def maxProduct(self, nums):
        n, r = len(nums), nums[0]
        maxValue, minValue = [nums[:1] + [0] * (n - 1) for _ in range(2)]

        for i in range(1, n):
            candidates = (
                maxValue[i - 1] * nums[i], minValue[i - 1] * nums[i], nums[i])
            maxValue[i], minValue[i] = max(candidates), min(candidates)
            r = max(r, maxValue[i])
        return r


class Solution(object):
    '''算法思路：

    同上，不过不用数组，而是改用两个变量表示最大最小乘积值

    Time: O(n)
    Space: O(1)
    '''
    def maxProduct(self, nums):
        n = len(nums)
        r = maxValue = minValue = nums[0]

        for i in range(1, n):
            candidates = (minValue * nums[i], maxValue * nums[i], nums[i])
            maxValue, minValue = max(candidates), min(candidates)
            r = max(maxValue, r)
        return r


s = Solution()
print s.maxProduct([0, 2, -1, -9])
