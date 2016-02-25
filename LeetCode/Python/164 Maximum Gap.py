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

    Time: O(n)
    '''
    def bucketSort(self, nums, i):
        container = [[] for _ in xrange(10)]
        for num in nums:
            container[ord(num[i]) - 48].append(num)
        return sum(container, [])

    def radixSort(self, nums, k):
        for i in xrange(k - 1, -1, -1):
            nums = self.bucketSort(nums, i)
        return nums

    def maximumGap(self, nums):
        nums = map(str, nums)
        k = max(map(len, nums) or [0])

        nums = map(int, self.radixSort(
            map(lambda num: '0' * (k - len(num)) + num, nums), k))

        return max([
            nums[i] - nums[i - 1] for i in xrange(1, len(nums))
        ] or [0])


import math


class Solution(object):
    '''算法思路：

    桶排序，关键点在于如何确定桶的大小

    maximum_gap >= (end - start + 1) / (n - 1) > (end - start + 1) / n

    所以桶大小可以确定为 size = (end - start + 1) / n，且维护每个桶的中最大最小值，
    同一个桶中差值必定小于 size，因此只需找到相邻桶间的 maximum_gap 即可

    Time: O(n)
    '''
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0

        start, end = min(nums), max(nums)

        size = max((end - start + 1) / n, 1)
        length = int(math.ceil(float(end - start + 1) / size))

        buckets = [None for _ in xrange(length)]
        for num in nums:
            i = (num - start) / size
            buckets[i] = (
                [min(buckets[i][0], num), max(buckets[i][1], num)]
                if buckets[i] else [num, num]
            )

        buckets = filter(None, buckets)
        return max([
            buckets[i][0] - buckets[i - 1][1]
            for i in xrange(1, len(buckets))
        ] or [0])


s = Solution()
print s.maximumGap([1,10000000])
