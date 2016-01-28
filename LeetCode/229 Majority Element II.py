# -*- coding: utf-8 -*-

'''
Majority Element II
===================

Given an integer array of size n, find all elements that appear more than
⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
'''


import collections


class Solution(object):
    '''算法思路：

    运用了 hash，所以不符合 O(1) space 的要求
    '''
    def majorityElement(self, nums):
        least = len(nums) / 3
        return [
            num for num, count in collections.Counter(nums).items()
            if count > least]


class Solution(object):
    '''算法思路：

    其实也是 Moore Voting Algorithm

    参考了：https://leetcode.com/discuss/42829/6-lines-general-case-o-n-time-and-o-k-space
    '''
    def majorityElement(self, nums):
        counter = collections.Counter()
        for num in nums:
            counter[num] += 1
            if len(counter) == 3:
                counter -= collections.Counter(set(counter))
        return [num for num in counter if nums.count(num) > len(nums) / 3]


s = Solution()
print s.majorityElement([1, 3])
