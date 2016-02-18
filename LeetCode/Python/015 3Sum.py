# -*- coding: utf-8 -*-

'''
3Sum
====

Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0?

Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4},

A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''


class Solution(object):
    '''算法思路：

    a + b + c = 0 -> a + b = -c
    于是就转换成了 Two Sum，对于每一个数的相反数求 Two Sum 的所有结果

    复杂度: O(n^2)
    '''
    def threeSum(self, nums):
        r, visited = set(), set()
        for i, target in enumerate(nums):
            if target in visited:
                continue

            record = set()
            for j, num in enumerate(nums):
                if i == j:
                    continue

                left = -target - num
                if left in record:
                    r.add(tuple(sorted([target, left, num])))
                record.add(num)
            visited.add(target)
        return list(r)


class Solution(object):
    '''算法思路：

    首先对 nums 进行排序，然后遍历 nums，对于每一个 num，对 num 后的序列两边加逼，
    找出符合条件的数字
    '''

    def threeSum(self, nums):
        nums, i = sorted(nums), 0

        results = set()
        while i < len(nums) - 2:
            low, high = i + 1, len(nums) - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if s < 0:
                    low += 1
                elif s > 0:
                    high -= 1
                else:
                    results.add((nums[i], nums[low], nums[high]))
                    low += 1
            i += 1

        return list(results)


class Solution(object):
    '''算法思路：

    同上，不过这次却巧妙去重
    '''
    def threeSum(self, nums):
        nums, n, r = sorted(nums), len(nums), []
        for i, target in enumerate(nums):
            if i and nums[i - 1] == target:
                continue

            j, k = i + 1, n - 1
            while j < k:
                sum = nums[j] + nums[k]
                if sum > -target:
                    k -= 1
                elif sum < -target:
                    j += 1
                else:
                    r.append([target, nums[j], nums[k]])
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    j += 1
        return r


s = Solution()
print s.threeSum([-1, -1, 0, 1, 2])
