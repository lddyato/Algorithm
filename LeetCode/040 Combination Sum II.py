# -*- coding: utf-8 -*-

'''
Combination Sum II
==================

Given a collection of candidate numbers (C) and a target number (T), find all
unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

- All numbers (including target) will be positive integers.
- Elements in a combination (a1, a2, … , ak) must be in non-descending order.
  (ie, a1 ≤ a2 ≤ … ≤ ak).
- The solution set must not contain duplicate combinations.

For example, given candidate set 10,1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''


class Solution(object):
    '''算法思路：

    同 I，但是每次去掉已经使用的
    '''
    def search(self, candidates, target):
        if target < 1:
            return []

        r = set()
        for i, num in enumerate(candidates):
            if num > target:
                break

            if num == target:
                r.add((num,))
                break

            left = self.search(candidates[i+1:], target - num)

            if left:
                r |= set(tuple([num] + p) for p in left)

        return map(list, r)

    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.search(candidates, target)


s = Solution()
print s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
