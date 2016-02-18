# -*- coding: utf-8 -*-

'''
Two Sum II - Input array is sorted
==================================

Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2. Please note that your
returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''


class Solution(object):
    '''算法思路：

    两边加逼
    '''
    def twoSum(self, nums, target):
        low, high = 0, len(nums) - 1

        while low < high:
            s = nums[low] + nums[high]

            if s > target:
                high -= 1
            elif s < target:
                low += 1
            else:
                return low + 1, high + 1


s = Solution()
print s.twoSum([2, 7, 11, 15], 9)
