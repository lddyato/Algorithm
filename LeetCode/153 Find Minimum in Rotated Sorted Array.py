# -*- coding: utf-8 -*-

'''
Find Minimum in Rotated Sorted Array
====================================

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''


class Solution(object):
    '''算法思路：

    二分查找
    '''
    def findMin(self, nums):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] > nums[-1]:
                low = mid + 1
            else:
                if mid > 0 and nums[mid - 1] > nums[-1] or mid == 0:
                    return nums[mid]
                high = mid - 1

        return nums[low]
