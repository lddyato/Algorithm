# -*- coding: utf-8 -*-

'''
Contains Duplicate II
=====================

Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and the
difference between i and j is at most k.
'''


class Solution(object):
    '''算法思路：

    hash 记录 num 上次出现的 index
    '''
    def containsNearbyDuplicate(self, nums, k):
        record = {}
        for i, num in enumerate(nums):
            if num in record and i - record[num] <= k:
                return True
            record[num] = i
        return False
