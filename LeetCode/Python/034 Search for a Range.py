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


def bisect_left(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + high >> 1

        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            if mid == 0 or nums[mid - 1] < target:
                return mid
            high = mid - 1
    return -1


def bisect_right(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + high >> 1
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            if mid == len(nums) - 1 or nums[mid + 1] > target:
                return mid
            low = mid + 1
    return -1


class Solution(object):
    '''算法思路：

    二分查找, 自己实现
    '''
    def searchRange(self, nums, target):
        return [bs(nums, target) for bs in (bisect_left, bisect_right)]


import bisect


class Solution(object):
    '''算法思路：

    使用内置库函数实现
    '''
    def searchRange(self, nums, target):
        start, end = [
            bs(nums, target)
            for bs in (bisect.bisect_left, bisect.bisect_right)
        ]

        if start >= len(nums) or nums[start] != target:
            return [-1, -1]

        return [start, end - 1]


s = Solution()
print s.searchRange([5, 7, 7, 8, 8, 10], 4)
