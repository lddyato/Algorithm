# -*- coding: utf-8 -*-

'''
Search in Rotated Sorted Array
==============================

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.
'''


class Solution(object):
    '''算法思路：

    二分法查找，需要讨论何时 low = mid + 1, 以及何时 high = mid - 1

    - 当 target 在前半部分，且 nums[mid] 也在前半部分，且 nums[mid] < target
    - 当 target 在后半部分, 且 not (nums[mid] 也在第二部分，且 nums[mid] > target)

    上述两种情况下 low = mid + 1，其余情况下 high = mid + 1
    '''
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + high >> 1
            if nums[mid] == target:
                return mid

            if (target < nums[0] and not target < nums[mid] < nums[0] or
                    target >= nums[0] and nums[0] <= nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1
        return -1


s = Solution()
print s.search([4, 5, 6, 7, 8, 0, 1, 2, 3], 1)
