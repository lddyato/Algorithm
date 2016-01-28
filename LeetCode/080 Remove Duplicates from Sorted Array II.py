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

    遍历 nums，对于每一个 num，分情况：

    - 如果下一个数和 num 相等，则删除所有和下一个数挨着的、且和 num 相等的下下一个数，
    并且把下标置为下下一个数

    - 否则，直接把下标置为下一个数
    '''
    def removeDuplicates(self, nums):
        i = 0

        while i < len(nums):
            j = i + 1

            if j < len(nums) and nums[i] == nums[j]:
                k = j + 1
                while k < len(nums) and nums[k] == nums[j]:
                    del nums[k]
                i = k
            else:
                i = j

        return len(nums)


s = Solution()
print s.removeDuplicates([0, 0, 0, 0])
