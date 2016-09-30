# -*- coding: utf-8 -*-

'''
Remove Duplicates from Sorted Array
===================================

Given a sorted array, remove the duplicates in place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with
constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums
being 1 and 2 respectively. It doesn't matter what you leave beyond the new
length.
'''


class Solution(object):
    '''算法思路：

    遍历 nums，对于每一个 num，如果下一个数和 num 相等就删掉。

    这个题的一个坑是：不能只计算 length 而不改变 nums
    '''
    def removeDuplicates(self, nums):
        i = 0

        while i < len(nums):
            j = i + 1

            while j < len(nums) and nums[j] == nums[i]:
                del nums[j]

            i = j

        return len(nums)


class Solution(object):
    '''算法思路：

    不需改变数组长度，填充式
    '''
    def removeDuplicates(self, nums):
        pointer = 0
        for num in nums:
            if pointer == 0 or num != nums[pointer - 1]:
                nums[pointer] = num
                pointer += 1
        return pointer


class Solution(object):
    '''算法思路：

    同样不需改变数组长度，交换式
    '''
    def removeDuplicates(self, nums):
        n = len(nums)

        if n < 2:
            return n

        low, high = 0, 0
        while high < n:
            if nums[high] != nums[low]:
                low += 1
                nums[low], nums[high] = nums[high], nums[low]
            high += 1
        return low + 1


s = Solution()
print s.removeDuplicates([1, 1, 2])
