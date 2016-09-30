# -*- coding: utf-8 -*-

"""
Combination Sum IV
==================

Given an integer array with all positive numbers and no duplicates, find the
number of possible combinations that add up to a positive integer target.

Example:

    nums = [1, 2, 3]
    target = 4

    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)

    Note that different sequences are counted as different combinations.

    Therefore the output is 7.

Follow up:

    - What if negative numbers are allowed in the given array?
    - How does it change the problem?
    - What limitation we need to add to the question to allow negative numbers?
"""


def cache(f):
    def method(obj, nums, target):
        if target not in obj.record:
            obj.record[target] = f(obj, nums, target)
        return obj.record[target]
    return method


class Solution(object):
    @cache
    def search(self, nums, target):
        if target == 0:
            return 1

        if not nums or target < 0:
            return 0

        return sum([self.search(nums, target - num) for num in nums])

    def combinationSum4(self, nums, target):
        self.record = {}
        return self.search(nums, target)


s = Solution()
print s.combinationSum4([4, 2, 1], 32)

