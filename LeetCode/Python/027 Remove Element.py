# -*- coding: utf-8 -*-

'''
Remove Element
==============

Given an array and a value, remove all instances of that value in place and
return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond
the new length.
'''


class Solution(object):
    '''算法思路：

    two pointers
    '''
    def removeElement(self, nums, val):
        low, high, r = 0, len(nums) - 1, 0
        while 1:
            while low < len(nums) and nums[low] != val:
                low += 1
                r += 1

            while high >= 0 and nums[high] == val:
                high -= 1

            if low >= high:
                break

            nums[low], nums[high] = nums[high], nums[low]
        return r


class Solution(object):
    '''算法思路：

    填充
    '''
    def removeElement(self, nums, val):
        pointer = 0
        for num in nums:
            if num != val:
                nums[pointer] = num
                pointer += 1
        return pointer

s = Solution()
print s.removeElement([3, 3], 3)
