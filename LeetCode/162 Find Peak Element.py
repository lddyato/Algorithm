# -*- coding: utf-8 -*-

'''
Find Peak Element
=================

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return
its index.

The array may contain multiple peaks, in that case return the index to any one
of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function
should return the index number 2.

Note:
Your solution should be in logarithmic complexity.
'''


class Solution(object):
    '''算法思路：

    直接遍历，由于要求是 O(log(n))，因此不符合要求

    Time: O(n)
    '''
    def findPeakElement(self, nums):
        for i, num in enumerate(nums):
            if (i > 0 and nums[i - 1] < num or i == 0) and (
                    i + 1 < len(nums) and num > nums[i + 1] or
                    i + 1 == len(nums)):
                return i


class Solution(object):
    '''算法思路：

    二分查找

    Time: O(log(n))
    '''
    def findPeakElement(self, nums):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if mid and nums[mid] < nums[mid - 1]:
                high = mid - 1
            elif mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                return mid


s = Solution()
print s.findPeakElement([2, 1, 2])
