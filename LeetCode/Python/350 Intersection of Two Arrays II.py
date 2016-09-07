#!/usr/bin/env python
# encoding: utf-8

"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
  - Each element in the result should appear as many times as it shows in both
    arrays.
  - The result can be in any order.

Follow up:
  - What if the given array is already sorted? How would you optimize your
    algorithm?
  - What if nums1's size is small compared to num2's size? Which algorithm is
    better?
  - What if elements of nums2 are stored on disk, and the memory is limited
    such that you cannot load all elements into the memory at once?
"""


import collections


class Solution(object):
    """算法思路：

    统计每个数出现次数，然后计算出相同key出现的最小次数
    """
    def intersect(self, nums1, nums2):
        counter1, counter2 = map(collections.Counter, (nums1, nums2))
        return sum([
            [key] * min(counter1[key], counter2[key])
            for key in set(counter1) & set(counter2)
        ], [])


class Solution(object):
    """Follow Up 1:

    双指针
    """
    def intersect(self, nums1, nums2):
        p1, p2, m, n, r = 0, 0, len(nums1), len(nums2), []
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                r.append[nums1[p1]]
                p1 += 1
                p2 += 1
        return r


s = Solution()
print s.intersect([1, 2, 2, 3], [2, 2, 2, 2])
