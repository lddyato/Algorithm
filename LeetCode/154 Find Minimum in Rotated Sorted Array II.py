# -*- coding: utf-8 -*-

'''
Find Minimum in Rotated Sorted A rray II
=======================================

    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''


class Solution(object):
    '''算法思路：

    二分查找，先将两边的相等的去掉，剩下的就和 I 一样了
    '''
    def findMin(self, nums):
        low, high = 0, len(nums) - 1
        while low < high and nums[low] == nums[high]:
            low += 1

        while low <= high:
            mid = (low + high) / 2
            if nums[mid] > nums[-1]:
                low = mid + 1
            else:
                if mid > 0 and nums[mid - 1] > nums[-1] or mid == 0:
                    return nums[mid]
                high = mid - 1

        return nums[low]


s = Solution()
print s.findMin([4, 1, 4])
