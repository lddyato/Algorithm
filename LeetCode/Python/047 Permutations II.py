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
            tuple((v,) + p for p in self.permuteUnique(nums[:i] + nums[i + 1:]))
            for i, v in enumerate(nums)], ())))


class Solution(object):
    '''算法思路：

    对每一层，如果已经遍历过了，则不再遍历

    结果：Accepted
    '''
    def search(self, nums):
        if len(nums) == 1:
            return [nums]

        record, r = set(), []
        for i, num in enumerate(nums):
            if num in record:
                continue
            r += [[num] + path for path in self.search(nums[:i] + nums[i + 1:])]
            record.add(num)
        return r

    def permuteUnique(self, nums):
        if not nums:
            return []
        return self.search(nums)


class Solution(object):
    """算法思路：

    同I，利用动态规划的思想，根据前n个序列，生成长度为n+1的序列
    """
    def permuteUnique(self, nums):
        r = [[]]
        for num in nums:
            new_r = []
            for path in r:
                for i in xrange(len(path) + 1):
                    new_r.append(path[:i] + [num] + path[i:])
                    if i < len(path) and path[i] == num:
                        break
            r = new_r
        return r


s = Solution()
print s.permuteUnique([1, 1, 2])
