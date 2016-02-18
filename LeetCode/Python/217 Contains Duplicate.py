# -*- coding: utf-8 -*-

'''
Contains Duplicate
==================

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.
'''


class Solution(object):
    '''算法思路：

    hash，记录已经存在的数字

    Time: O(n)
    Space: O(n)
    '''
    def containsDuplicate(self, nums):
        record = {}
        for n in nums:
            if n in record:
                return True
            record[n] = 1
        return False


class Solution(object):
    '''算法思路：

    形成集合，如果集合的长度与数组的长度不相等，那么一定存在重复数字

    Time: O(n)
    Space: O(n)
    '''
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)


class Solution(object):
    '''算法思路：

    排序，然后挨着的两个数字比较是否相等

    Time: O(n*log(n))
    Space: O(1)
    '''
    def containsDuplicate(self, nums):
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                return True
            i += 1
        return False
