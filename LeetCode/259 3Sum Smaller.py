# -*- coding: utf-8 -*-

'''
3Sum Smaller
============

Given an array of n integers nums and a target, find the number of index
triplets i, j, k with 0 <= i < j < k < n that satisfy the condition
nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:
    [-2, 0, 1]
    [-2, 0, 3]
'''


class Solution(object):
    '''算法思路：

    也是先排序，然后两边加逼。

    这类题型可以看成是 固定 i 和 low, 移动 high 找出符合条件的结果，然后再移动 low、i
    继续寻找
    '''
    def threeSumSmaller(self, nums, target):
        maps, i, result = sorted(enumerate(nums), key=lambda n: n[1]), 0, 0

        while i < len(nums) - 2:
            low, high = i + 1, len(nums) - 1

            while low < high:
                s = maps[i][1] + maps[low][1] + maps[high][1]
                if s < target:
                    result += high - low
                    low += 1
                else:
                    high -= 1

            i += 1

        return result

s = Solution()
print s.threeSumSmaller([-2, 0, 1, 3], 4)
