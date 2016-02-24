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


class Solution(object):
    '''算法思路：

    对于最多 k 个重复的数字，普遍做法，用双指针，并用一个变量记录当前重复填充了多少个
    '''
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        n, slow, fast, cnt, k = len(nums), 0, 1, 1, 2
        while fast < n:
            if nums[fast] != nums[slow] or cnt < k:
                cnt = 1 if nums[fast] != nums[slow] else (cnt + 1)
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


s = Solution()
print s.removeDuplicates([0, 0, 0, 0])
