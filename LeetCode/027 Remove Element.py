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
    def removeElement(self, nums, val):
        i = 0

        while i < len(nums):
            while i < len(nums) and val == nums[i]:
                del nums[i]

            i += 1

        return len(nums)


s = Solution()
print s.removeElement([3, 3], 3)
