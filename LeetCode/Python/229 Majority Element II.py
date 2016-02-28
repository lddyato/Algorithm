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

    Moore Voting Algorithm，维护数量最多的两个

    Time: O(n)
    Space: O(1)
    '''
    def majorityElement(self, nums):
        first, second, cntFirst, cntSecond, n = None, None, 0, 0, len(nums)
        for num in nums:
            if num != first and num != second:
                if not cntFirst:
                    first, cntFirst = num, 1
                elif not cntSecond:
                    second, cntSecond = num, 1
                else:
                    cntFirst -= 1
                    cntSecond -= 1
            elif num == first:
                cntFirst += 1
            else:
                cntSecond += 1

        return [item for item in (first, second) if nums.count(item) > n/3]


class Solution(object):
    '''算法思路：

    Moore Voting Algorithm 更一般的形式

    对于求出所有多于 n/k 个元素，维护 k 个变量，当当前 num 与 k 个变量都不相同时，所有 k 个
    变量 -1，因为数量是相对于的

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
