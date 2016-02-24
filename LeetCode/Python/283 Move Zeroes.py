# -*- coding: utf-8 -*-

'''
Move Zeroes
===========

Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution(object):
    '''算法思路：

    类似于冒泡排序，从前往后

    Time: O(n^2)
    '''
    def moveZeroes(self, nums):
        i, end = 0, len(nums) - 1
        while i < end:
            if nums[i] != 0:
                i += 1
                continue

            j = i
            while j < end:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j += 1

            end -= 1


class Solution(object):
    '''算法思路：

    类似于冒泡排序，从后往前

    Time: O(n^2)
    '''
    def moveZeroes(self, nums):
        end = len(nums) - 1
        while end >= 0 and nums[end] == 0:
            end -= 1

        i = end - 1
        while i >= 0:
            if nums[i] != 0:
                i -= 1
                continue

            j = i
            while j < end:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j += 1

            end -= 1


class Solution(object):
        '''算法思路：

    从前往后，遇到非0数字就往前靠（不是交换，而是赋值），最后剩余的填充为0

    这种做法的依据是，因为知道最后要填充的数字为0，因此只需关心非0数字即可

    Time: O(n)
    '''
    def moveZeroes(self, nums):
        tail = 0
        for i, num in enumerate(nums):
            if num:
                nums[tail] = num
                tail += 1
        nums[tail:] = [0] * (len(nums) - tail)


class Solution(object):
    '''算法思路：

    换一种思路，把非零的往前挪

    Time: O(n)
    '''
    def moveZeroes(self, nums):
        slow, fast, n = 0, 0, len(nums)
        while fast < n:
            if nums[fast]:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1


class Solution(object):
    '''算法思路：

    排序

    Time: O(n*log(n))
    '''
    def moveZeroes(self, nums):
        nums.sort(cmp=lambda x, y: [1, -1][y == 0])


s = Solution()
s.moveZeroes([0, 1, 2, 0, 3, 12])
