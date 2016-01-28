# -*- coding: utf-8 -*-

'''
3Sum Closest
============

Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    '''算法思路：

    先排序，然后两边加逼
    '''
    def threeSumClosest(self, nums, target):
        nums, i, m = sorted(nums), 0, None

        while i < len(nums) - 2:
            low, high = i + 1, len(nums) - 1

            while low < high:
                s = nums[i] + nums[low] + nums[high]
                distince = abs(target - s)

                if m is None or distince < m:
                    m = distince
                    result = s

                if s < target:
                    low += 1
                else:
                    high -= 1

            i += 1
        return result

s = Solution()
print s.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82)
