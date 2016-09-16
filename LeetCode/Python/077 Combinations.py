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
    def search(self, nums, k):
        if k == 1:
            return [[num] for num in nums]

        r = []
        for i, num in enumerate(nums):
            left = nums[i + 1:]
            if len(left) < k - 1:
                break

            r += [[num] + path for path in self.search(left, k - 1)]

        return r

    def combine(self, n, k):
        return self.search(range(1, n + 1), k)


s = Solution()
print s.combine(1, 1)
