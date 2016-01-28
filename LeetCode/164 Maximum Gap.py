# -*- coding: utf-8 -*-

'''
Maximum Gap
===========

Given an unsorted array, find the maximum difference between the successive
elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in
the 32-bit signed integer range.
'''


class Solution(object):
    '''算法思路：

    Radix Sort，基数排序
    '''
    def countingSort(self, nums, i):
        container = [[] for _ in xrange(10)]
        for num in nums:
            container[ord(num[i]) - 48].append(num)
        return sum(container, [])

    def radixSort(self, nums, k):
        for i in xrange(k - 1, -1, -1):
            nums = self.countingSort(nums, i)
        return nums

    def maximumGap(self, nums):
        nums = map(str, nums)
        k = max(map(len, nums) or [0])

        nums = map(int, self.radixSort(
            map(lambda num: '0' * (k - len(num)) + num, nums), k))

        return max([v - nums[i - 1] for i, v in enumerate(nums[1:], 1)] or [0])


s = Solution()
print s.maximumGap([1,10000000])
