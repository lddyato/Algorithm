# -*- coding: utf-8 -*-

'''
Subsets II
==========

Given a collection of integers that might contain duplicates, nums, return all
possible subsets.

Note:
- Elements in a subset must be in non-descending order.
- The solution set must not contain duplicate subsets.

For example,

If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution(object):
    '''算法思路：

    对于每个元素都存在选中与不选中两种选择
    '''
    def subsets(self, nums):
        if not nums:
            return set([()])

        left = self.subsets(nums[1:])
        return set(tuple(nums[:1]) + p for p in left) | left

    def subsetsWithDup(self, nums):
        nums.sort()
        return map(list, self.subsets(nums))


s = Solution()
print s.subsetsWithDup([1, 2, 2])
