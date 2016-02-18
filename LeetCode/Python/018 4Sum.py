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
    '''算法思路：

    都是先排序，然后两边加逼
    '''
    def fourSum(self, nums, target):
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


class Solution(object):
    '''算法思路：

    同上，只不过不在用 set 去重
    '''
    def fourSum(self, nums, target):
        nums, n, r = sorted(nums), len(nums), []
        for i in xrange(n - 3):
            if i and nums[i] == nums[i - 1]:
                continue

            for j in xrange(n - 1, i + 2, -1):
                if j < n - 1 and nums[j] == nums[j + 1]:
                    continue

                low, high, t = i + 1, j - 1, target - nums[i] - nums[j]
                while low < high:
                    sum = nums[low] + nums[high]
                    if sum < t:
                        low += 1
                    elif sum > t:
                        high -= 1
                    else:
                        r.append([nums[i], nums[low], nums[high], nums[j]])
                        while low < high and nums[low + 1] == nums[low]:
                            low += 1
                        while low < high and nums[high - 1] == nums[high]:
                            high -= 1
                        low += 1
        return r
