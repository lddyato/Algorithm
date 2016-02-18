# -*- coding: utf-8 -*-

'''
Combinations
============

Given two integers n and k, return all possible combinations of k numbers out
of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution(object):
    '''算法思路:

    暴力递归
    '''
    def _gen_combine(self, nums, steps):
        if steps == 1:
            return [[n] for n in nums]

        return sum([
            [[v] + p for p in self._gen_combine(nums[i+1:], steps-1)]
            for i, v in enumerate(nums)
        ], [])

    def combine(self, n, k):
        return self._gen_combine(range(1, n + 1), k)


s = Solution()
print s.combine(1, 1)
