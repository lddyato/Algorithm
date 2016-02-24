# -*- coding: utf-8 -*-

'''
Search in Rotated Sorted Array II
=================================

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''


class Solution(object):
    '''算法思路：

    同 I，不过需要把序列末尾和头部重复的数字去掉
    '''
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low < high and nums[low] == nums[high]:
            high -= 1

        while low <= high:
            mid = low + high >> 1
            if nums[mid] == target:
                return True

            if (target >= nums[0] and nums[0] <= nums[mid] < target or
                    target < nums[0] and not target < nums[mid] < nums[0]):
                low = mid + 1
            else:
                high = mid - 1
        return False


s = Solution()
print s.search([3, 1, 1], 1)
