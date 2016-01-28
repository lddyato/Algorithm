# -*- coding: utf-8 -*-

'''
Wiggle Sort
===========

Given an unsorted array nums, reorder it in-place such that
nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is
[1, 6, 2, 5, 3, 4].
'''


class Solution(object):
    '''算法思路：

    先排序，然后从中间折叠

    Time: O(n*log(n))
    Space: O(n)
    '''
    def wiggleSort(self, nums):
        if len(nums) < 2:
            return

        nums.sort()

        i, n, copy = 0, len(nums), nums[:]
        for i in xrange(len(nums)):
            j = 2 * i if i <= (n - 1) / 2 else ((n - i - 1) * 2 + 1)
            nums[j] = copy[i]


class Solution(object):
    '''算法思路：

    完美洗牌算法

    Time: O(n*log(n))，主要是排序，完美洗牌算法为 O(n)
    Space: O(1)
    '''
    def reverse(self, start, end):
        low, high = start, end
        while low < high:
            self.nums[low], self.nums[high] = self.nums[high], self.nums[low]
            low += 1
            high -= 1

    def getK(self, n):
        k, square = 1, 3
        while square - 1 <= 2 * n:
            k += 1
            square *= 3
        return k - 1

    def shuffle(self, start, end):
        n = (end - start + 1) / 2

        k = self.getK(n)
        m = (3 ** k - 1) / 2
        if m != n:
            self.reverse(start + m, start + n - 1)
            self.reverse(start + n, start + n + m - 1)
            self.reverse(start + m, start + n + m - 1)

        for k in xrange(1, k + 1):
            i = cursor = 3 ** (k - 1)
            pre, visited = self.nums[i + start - 1], False
            while not (i == cursor and visited):
                i = (2 * i) % (2 * m + 1)
                self.nums[i + start - 1], pre = pre, self.nums[i + start - 1]

                if not visited:
                    visited = True

        if n != m:
            self.shuffle(start + 2 * m, end)

    def wiggleSort(self, nums):
        length = len(nums)
        if length < 2:
            return

        nums.sort()

        start, end = 1, length - 1
        if not length & 1:
            end -= 1

        self.nums = nums
        self.shuffle(start, end)


class Solution(object):
    '''算法思路：

    分奇偶

    - 当 i 为偶数时，如果 nums[i] > nums[i - 1]，则交换 nums[i] 和 nums[i - 1]
    - 当 i 为奇数时，如果 nums[i] < nums[i - 1]，则交换 nums[i] 和 nums[i - 1]
    '''
    def wiggleSort(self, nums):
        for i in xrange(1, len(nums)):
            if (i & 1 and nums[i] < nums[i - 1] or
                    not i & 1 and nums[i] > nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]


s = Solution()
s.wiggleSort([3, 1, 4, 8, 2, 9])
