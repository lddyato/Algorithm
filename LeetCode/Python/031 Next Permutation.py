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
    """算法思路：

    首先我们要找Next Permutation具有什么样的特征。Next肯定要比当前序列大，我们
    要从后往前对每一个字符，找到它后边是否有比它大的，如果有，找出比他大的序列
    中最小的那个，然后置换，最后对其后边的元素反转。

    有一个特性，该字符后边的序列是递减序列。

    例如: 2 8 1 6 9 8 7 2

    从后往前遍历，到6这个数字的时候，7、8、9都比6大，我们要找出比6大的序列中
    最小的那个，这里是7，然后把6和7置换，变成了

    2 8 1 7 9 8 6 2

    然后再把7后边的这个递减序列反转，变成

    2 8 1 7 2 6 8 9

    这样就能保证是比原序列大的最小的那个
    """
    def search(self, nums, start, end, target):
        # binary search to get the index which is the smallest one larger than
        # target
        low, high = start, end
        while low <= high:
            mid = low + high >> 1
            if nums[mid] <= target:
                high = mid - 1
            else:
                if mid == end or nums[mid + 1] <= target:
                    return mid
                low = mid + 1

    def reverse(self, nums, start, end):
        # reverse the nums[start:end + 1] in place
        low, high = start, end
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1

    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return

        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        if i >= 0:
            x = self.search(nums, i + 1, n - 1, nums[i])
            nums[i], nums[x] = nums[x], nums[i]

        self.reverse(nums, i + 1, n - 1)


s = Solution()
s.nextPermutation([1, 2, 3, 4, 6, 5, 2, 1])
s.nextPermutation([1, 2])
