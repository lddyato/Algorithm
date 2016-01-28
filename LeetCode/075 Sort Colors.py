# -*- coding: utf-8 -*-

'''
Sort Colors
===========

Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red,
white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''


class Solution(object):
    '''算法思路：

    计数排序，适用于 数的大小范围 < 100 的这种情况
    '''
    def sortColors(self, nums):
        record = [0] * 3
        for n in nums:
            record[n] += 1

        s = 0
        for i in xrange(len(record)):
            for j in xrange(record[i]):
                nums[s] = i
                j += 1
                s += 1


class Solution(object):
    def sortColors(self, nums):
        i, low, high = 0, 0, len(nums) - 1
        while low <= i <= high:
            if nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
                continue

            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1

            i += 1

e
s = Solution()
print s.sortColors([0, 2, 1])
