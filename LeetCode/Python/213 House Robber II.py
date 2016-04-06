# -*- coding: utf-8 -*-

'''
House Robber II
===============

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new
place for his thievery so that he will not get too much attention. This time,
all houses at this place are arranged in a circle. That means the first house
is the neighbor of the last one. Meanwhile, the security system for these
ouses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.
'''


class Solution(object):
    '''算法思路：

    可以分两种情况，nums[0] 选中 和 不选中，选中了那说明 nums[1] 和 nums[-1] 都不可
    以被选中，求 nums[2:-1] 的最大值即可，如果没选中，那么求 nums[1:] 的最大值即可
    '''
    def robLine(self, nums):
        dp = [0] * (len(nums) + 2)
        for i, num in enumerate(nums, 2):
            dp[i] = max(dp[i - 1], dp[i - 2] + num)
        return dp[-1]

    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        return max(map(self.robLine, (nums[1:], nums[:-1])))


s = Solution()
print s.rob([])
