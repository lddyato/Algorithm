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
    """算法思路：

    增加了个数的限制
    """
    def search(self, k, target, start):
        if k <= 0 or start > 9:
            return []

        r = []
        for i in xrange(start, 10):
            if target == i:
                if k == 1:
                    r.append([i])
                continue

            if i > target:
                break

            r += [[i] + path for path in self.search(k - 1, target - i, i + 1)]

        return r

    def combinationSum3(self, k, n):
        return self.search(k, n, 1)


s = Solution()
print s.combinationSum3(3, 9)
