# -*- coding: utf-8 -*-

'''
Remove Duplicates from Sorted Array II
======================================

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums
being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''


class Solution(object):
    '''算法思路：

    依旧是填充的思路
    '''
    def removeDuplicates(self, nums):
        tail = 0
        for num in nums:
            if tail < 2 or num != nums[tail - 1] or num != nums[tail - 2]:
                nums[tail] = num
                tail += 1
        return tail


s = Solution()
print s.removeDuplicates([0, 0, 0, 0])
