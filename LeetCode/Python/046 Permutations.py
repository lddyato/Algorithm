# -*- coding: utf-8 -*-

'''
Permutations
============

Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''


class Solution(object):
    '''算法思路：

    暴力递归
    '''
    def permute(self, nums):
        if not nums:
            return nums

        if len(nums) == 1:
            return [nums]

        return sum([
            map(lambda p: [v] + p, self.permute(nums[:i] + nums[i+1:]))
            for i, v in enumerate(nums)], [])


s = Solution()
print s.permute([1, 1, 2, 2])
