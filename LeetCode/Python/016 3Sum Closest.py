# -*- coding: utf-8 -*-

'''
3Sum Closest
============

Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    '''算法思路：

    先排序，然后两边加逼
    '''
    def threeSumClosest(self, nums, target):
        nums, n, minDistance, r = sorted(nums), len(nums), float('inf'), 0

        for i in xrange(n):
            j, k = i + 1, n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                distance = abs(sum - target)

                if distance < minDistance:
                    minDistance = distance
                    r = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    return target
        return r


s = Solution()
print s.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82)
