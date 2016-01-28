# -*- coding: utf-8 -*-

'''
4Sum
====

Given an array S of n integers, are there elements a, b, c, and d in S such
that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order.
(ie, a ≤ b ≤ c ≤ d).
The solution set must not contain duplicate quadruplets.

For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''


class Solution(object):
    def fourSum(self, nums, target):
        '''算法思路：

        都是先排序，然后两边加逼
        '''
        nums, i, result = sorted(nums), 0, set()

        while i < len(nums) - 3:
            j = i + 1

            while j < len(nums) - 2:
                low, high = j + 1, len(nums) - 1

                while low < high:
                    s = nums[i] + nums[j] + nums[low] + nums[high]
                    if s < target:
                        low += 1
                    elif s > target:
                        high -= 1
                    else:
                        result.add((nums[i], nums[j], nums[low], nums[high]))
                        low += 1
                j += 1
            i += 1

        return list(result)
