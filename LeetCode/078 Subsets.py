# -*- coding: utf-8 -*-

'''
Subsets
=======

Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    '''算法思路：

    利用规律：nums 的每一位分别对应 bits（长度为len(nums)）的每一位
    '''
    def subsets(self, nums):
        nums.sort()

        r = []
        for i in xrange(2 ** len(nums)):
            subset, n = [], 0
            while i:
                if i & 1:
                    subset.append(nums[n])
                i >>= 1
                n += 1
            r.append(subset)

        return r


s = Solution()
print s.subsets([2, 3, 4, 5])