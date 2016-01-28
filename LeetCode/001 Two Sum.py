# -*- coding: utf-8 -*-

'''
Two Sum
=======

Given an array of integers, find two numbers such that they add up to a
specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2. Please note that your
returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''


class Solution(object):
    '''算法思路：

    首先为 nums 排序，并且每个 nums 的每个元素都附带了排序前的 index，然后两边加逼
    '''
    def twoSum(self, nums, target):
        maps = sorted(
            map(lambda item: (item[1], item[0] + 1), enumerate(nums)),
            key=lambda i: i[0])

        low, high = 0, len(maps) - 1
        while low < high:
            s = maps[low][0] + maps[high][0]

            if s < target:
                low += 1
            elif s > target:
                high -= 1
            else:
                i_1, i_2 = maps[low][1], maps[high][1]
                return (i_1, i_2) if i_1 < i_2 else (i_2, i_1)


class Solution(object):
    '''算法思路：

    将数值和其 [下标, 下标, ...] 形成hash，然后判断 target - n 是否在 hash 里边
    注意两种情况:
      - target - n 和 n 相等
      - target - n 和 n 不相等

    相对于下一种，这种方法能够更加方便的改以适用于更多情况
    '''
    def twoSum(self, nums, target):
        maps = {}
        for i, n in enumerate(nums):
            maps.setdefault(n, []).append(i + 1)

        for n in nums:
            left = target - n

            if left in maps:
                if left == n and len(maps[n]) > 1:
                    return maps[n][:2]

                if left != n:
                    index_1, index_2 = maps[n][0], maps[left][0]
                    if index_1 > index_2:
                        index_1, index_2 = index_2, index_1

                    return index_1, index_2


class Solution(object):
    '''算法思路：同上

    不同点在于:

    不用事先准备好hash，而是一遍而过，用一个 hash 存储 {n: index}，如果 target - n
    不在 hash 里边 (即没有命中)，那么就存储 {n: index}，否则意味着 target - n 和 n
    都在 nums 数组里边
    '''
    def twoSum(self, nums, target):
        maps = {}
        for i, n in enumerate(nums):
            left = target - n
            if left in maps:
                return (maps[left] + 1, i + 1)

            maps[n] = i


s = Solution()
print s.twoSum([3, 2, 4, 2], 6)
print s.twoSum([0, 4, 2, 0], 0)
