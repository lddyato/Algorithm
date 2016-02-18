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
    '''
    def threeSumSmaller(self, nums, target):
        nums, n, r = sorted(nums), len(nums), 0
        for i, num in enumerate(nums):
            j, k, t = i + 1, n - 1, target - num
            while j < k:
                sum = nums[j] + nums[k]
                if sum < t:
                    r += k - j
                    j += 1
                else:
                    k -= 1
        return r


s = Solution()
print s.threeSumSmaller([-2, 0, 1, 3], 4)
