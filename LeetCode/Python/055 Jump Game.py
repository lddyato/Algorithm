# -*- coding: utf-8 -*-

'''
Jump Game
=========

Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''


class Solution(object):
    """算法思路：

    DFS 对于每一步都遍历，查找可行解

    Time: O(n^2)

    结果：TLE
    """
    def search(self, nums, i):
        if i >= len(nums):
            return True

        for step in xrange(1, nums[i] + 1):
            if self.search(nums, i + step):
                return True

        return False

    def canJump(self, nums):
        return self.search(nums, 0)


class Solution(object):
    '''算法思路：

    同上，不过用了动态规划

    Time: O(n^2)

    结果：TLE
    '''
    def canJump(self, nums):
        n = len(nums)

        dp = [False] * n
        dp[-1] = True

        for i in xrange(n - 2, -1, -1):
            dp[i] = any(
                dp[i + j] if i + j < n else True
                for j in xrange(1, nums[i] + 1)
            )

        return dp[0]


class Solution(object):
    '''算法思路：

    仔细分析，我们可以知道上述两种解法强行遍历有的步骤是浪费的，所以会TLE。

    计算最远能够达到的目标，如果最远能够达到的中途中断了，说明不能到最后，
    否则就能够达到最后一步

    贪心思路
    '''
    def canJump(self, nums):
        maxReach, n = 0, len(nums)
        for i in xrange(n):
            if maxReach < i:
                return False
            maxReach = max(maxReach, i + nums[i])

            if maxReach >= n - 1:
                return True

        return True


s = Solution()
s.canJump([2, 1, 0, 3])
