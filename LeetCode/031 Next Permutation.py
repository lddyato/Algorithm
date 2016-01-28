# -*- coding: utf-8 -*-

'''
Next Permutation
================

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest
possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its
corresponding outputs are in the right-hand column.

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
'''


class Solution(object):
    '''算法思路：

    从后向前，找到第一个 后边的数比紧挨着它的前面的数大的 数，然后交换 该数前一位 和
    该数后(算上该数)比该数大的最小值，最后对于该数及后面的值交换排序.
    '''
    def nextPermutation(self, nums):
        if len(nums) < 2:
            return

        i = len(nums) - 1

        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            nums.sort()
            return

        j = i
        while j < len(nums) and nums[j] > nums[i - 1]:
            j += 1

        nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]

        low, high = i, len(nums) - 1
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1


s = Solution()
s.nextPermutation([1, 2, 3, 4, 6, 5, 2, 1])
s.nextPermutation([1, 2])
