# -*- coding: utf-8 -*-

'''
Burst Balloons
==============

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number
on it represented by array nums. You are asked to burst all the balloons. If
the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and
right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can
    not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

    Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
    coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''


class Solution(object):
    '''算法思路：

    动态规划，设 dp[left][right] 为开区间 (left, right) 内最大 coins，则对于区间内
    每一个元素 nums[i] (其中 left < i < right)，将 nums[i] 看做最后一个爆破的气球，
    则递推方程式为：

    dp[l][r] = max(nums[l] * nums[i] * nums[r] + dp[l][i] + dp[i][r])
    '''
    def maxCoins(self, nums):
        nums = [1] + filter(None, nums) + [1]
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]

        for r in xrange(2, n):
            for left in xrange(n - r):
                right = left + r
                for i in xrange(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[i] * nums[right] +
                        dp[left][i] + dp[i][right]
                    )
        return dp[0][n - 1]


class Solution(object):
    '''算法思路：

    同上，只不过用缓存把结果保存起来
    '''
    def cache(f):
        def method(obj, nums, left, right):
            if obj.dp[left][right] is None:
                obj.dp[left][right] = f(obj, nums, left, right)
            return obj.dp[left][right]
        return method

    @cache
    def search(self, nums, left, right):
        return max([
            self.search(nums, left, i) + self.search(nums, i, right) +
            nums[i] * nums[left] * nums[right]
            for i in xrange(left + 1, right)] or [0]
        )

    def maxCoins(self, nums):
        nums = [1] + filter(None, nums) + [1]
        self.dp = [[None] * len(nums) for _ in xrange(len(nums))]
        return self.search(nums, 0, len(nums) - 1)


s = Solution()
print s.maxCoins([3,1,5,8])
