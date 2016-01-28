# -*- coding: utf-8 -*-

'''
Search for a Range
==================

Given a sorted array of integers, find the starting and ending position of a
given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,

Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution(object):
    '''算法思路：

    二分查找
    '''
    def searchLeft(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + high >> 1
            if nums[mid] < target:
                low = mid + 1
            else:
                if (nums[mid] == target and (mid and
                        nums[mid - 1] < target or not mid)):
                    return mid
                high = mid - 1
        return -1

    def searchRight(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + high >> 1
            if nums[mid] > target:
                high = mid - 1
            else:
                if (nums[mid] == target and (mid + 1 < len(nums) and
                        nums[mid + 1] > target or mid + 1 == len(nums))):
                    return mid
                low = mid + 1
        return -1

    def searchRange(self, nums, target):
        return [f(nums, target) for f in (self.searchLeft, self.searchRight)]


s = Solution()
print s.searchRange([5, 7, 7, 8, 8, 10], 4)
