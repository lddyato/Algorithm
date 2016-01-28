# -*- coding: utf-8 -*-

'''
Combination Sum III
===================

Find all possible combinations of k numbers that add up to a number n, given
that only numbers from 1 to 9 can be used and each combination should be a
unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.

Example 1:

    Input: k = 3, n = 7

    Output: [[1,2,4]]

Example 2:

    Input: k = 3, n = 9

    Output: [[1,2,6], [1,3,5], [2,3,4]]
'''


class Solution(object):
    def search2(self, candidates, target):
        r, record = [], {}
        for num in candidates:
            if target - num in record:
                r.append([min(num, target - num), max(num, target - num)])
            record[num] = True
        return r

    def search(self, candidates, target, k):
        return self.search2(candidates, target) if k == 2 else sum([[[num] + p
            for p in self.search(candidates[i+1:], target - num, k - 1)]
            for i, num in enumerate(candidates)], [])

    def combinationSum3(self, k, n):
        if k < 1:
            return []

        if k == 1:
            return [n] if 1 <= n <= 9 else []

        return self.search(range(1, 10), n, k)


s = Solution()
print s.combinationSum3(3, 9)
