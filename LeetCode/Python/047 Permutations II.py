# -*- coding: utf-8 -*-

'''
Permutations II
===============

Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''


class Solution(object):
    '''算法思路：

    用 set 去掉重复的序列

    结果：Time Limit Exceeded
    '''
    def permuteUnique(self, nums):
        if not nums:
            return nums

        if len(nums) == 1:
            return (tuple(nums),)

        return list(set(sum([
            tuple((v,) + p for p in self.permuteUnique(nums[:i] + nums[i+1:]))
            for i, v in enumerate(nums)], ())))


class Solution(object):
    '''算法思路：

    对每一层，如果已经遍历过了，则不再遍历

    结果：Accepted
    '''
    def permuteUnique(self, nums):
        exited = {}

        if not nums:
            return nums

        if len(nums) == 1:
            return [nums]

        result = []
        for i, v in enumerate(nums):
            if v not in exited:
                result.append([
                    [v] + p
                    for p in self.permuteUnique(nums[:i] + nums[i+1:])
                ])
                exited[v] = 1

        return sum(result, [])


s = Solution()
print s.permuteUnique([1, 1, 2])
