# -*- coding: utf-8 -*-

'''
First Missing Positive
======================

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''


class Solution(object):
    '''算法思路：

    将 nums 里边的数字转化为 hash，然后从小到大依次判断 first 是否在 hash 中

    Time: O(n)
    Space: O(n)
    '''
    def firstMissingPositive(self, nums):
        first, record = 1, {n: 0 for n in nums}
        while first in record:
            first += 1
        return first


class Solution(object):
    '''算法思路：

    观察到一个现象，first 一定在 [1, len(nums) + 1] 之间，因为 nums 最多占据前
    len(nums) 个正整数，由于每个 num 最多被访问 2 次，因此时间为 O(n)

    Time: O(n)
    Space: O(1)
    '''
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i, num in enumerate(nums):
            while (num is not None and 1 <= num <= n and
                    nums[num - 1] is not None):
                nums[num - 1], num = None, nums[num - 1]

        for i, num in enumerate(nums, 1):
            if num is not None:
                return i
        return n + 1


s = Solution()
print s.firstMissingPositive([2, 2])
