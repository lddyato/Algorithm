# -*- coding: utf-8 -*-

'''
Permutations
============

Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''


class Solution(object):
    """算法思路：

    对nums的每一个元素，令其为序列的第一个元素，如此循环。
    """
    def permute(self, nums):
        r = []
        for i, num in enumerate(nums):
            r += [
                [num] + path
                for path in self.permute(nums[:i] + nums[i + 1:]) or [[]]
            ]
        return r


class Solution(object):
    """算法思路：

    利用动态规划的思想，保存前n个元素的所有生成序列，然后对每一个序列，把当前
    元素插入到序列中的每一个位置
    """
    def permute(self, nums):
        r = [[]]
        for num in nums:
            r = [
                path[:i] + [num] + path[i:]
                for path in r
                for i in xrange(len(path), -1, -1)
            ]
        return r


s = Solution()
print s.permute([1, 1, 2, 2])
