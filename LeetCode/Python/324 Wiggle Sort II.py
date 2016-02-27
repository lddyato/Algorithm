# -*- coding: utf-8 -*-

'''
Wiggle Sort II
==============

Given an unsorted array nums, reorder it such that
nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
'''


class Solution(object):
    '''算法思路：

    关键点是要想到怎么样组合才能得到 nums[0] < nums[1] > nums[2] < nums[3]...
    而不会使临近的两个数相等

    如果正序从中间截开，然后把两部分合在一起，较小的一部分在偶数位置，较大的一部分在奇数位置，
    有可能重复，比如

    4, 5, 5, 6

    如果反序从中间截开，较小的一部分在偶数，较大的一部分在奇数，则不会重复，发生重复的时候
    较小的一部分 和 较大的一部分必定会有相同的元素，假设该元素为 M, 比该元素小的为 S，比该
    元素大的为 L，假设序列为： L, L, L, L, M, M, S, S, S, S，则重新组合后的序列为，可以
    看到相同的部分被隔离得最远

    M . S . S . S . S .
    . L . L . L . L . M

    Time: O(n)
    Space: O(n)
    '''
    def radixSort(self, nums):
        nums = map(str, nums)
        k = max(map(len, nums))
        nums = ['0' * (k - len(num)) + num for num in nums]

        for i in xrange(k - 1, -1, -1):
            buckets = [[] for _ in xrange(10)]
            for num in nums:
                buckets[ord(num[i]) - 48].append(num)
            nums = sum(buckets, [])
        return map(int, nums)

    def wiggleSort(self, nums):
        sortNums, n = self.radixSort(nums), len(nums) | 1
        for i, num in enumerate(sortNums[::-1]):
            nums[(2*i + 1) % n] = num


class Solution(object):
    '''算法思路：

    同上，不过用了内置的排序函数

    Time: O(nlog(n))
    Space: O(n)
    '''
    def wiggleSort(self, nums):
        nums.sort()
        n = len(nums)
        half = (n + (n & 1)) >> 1
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


class Solution(object):
    '''算法思路：

    同上，发现元素排放前和排放后是有规律的，即 i -> (2*i + 1) % n

    Time: O(nlog(n))
    Space: O(1)
    '''
    def wiggleSort(self, nums):
        for i, num in enumerate(sorted(nums, reverse=True)):
            nums[(1+2*i) % (len(nums)|1)] = num
