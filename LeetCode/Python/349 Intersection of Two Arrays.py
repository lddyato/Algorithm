#!/usr/bin/env python
# encoding: utf-8

"""
Intersection of Two Arrays
==========================

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


