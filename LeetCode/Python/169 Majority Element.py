# -*- coding: utf-8 -*-

'''
Majority Element
================

Given an array of size n, find the majority element. The majority element is
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.
'''


class Solution(object):
    '''算法思路：

    利用 hash 保存已经遍历过的值的个数，如果当前值的个数 >= mid 返回当前值

    Time: O(n)
    Space: O(n)
    '''
    def majorityElement(self, nums):
        n = len(nums)
        record, mid = {}, (n >> 1) + (n & 1)
        for i in nums:
            record[i] = record.setdefault(i, 0) + 1
            if record[i] >= mid:
                return i


class Solution(object):
    '''算法思路：

    排序后 index=n/2 处的值一定是 majority

    Time: O(n * log(n))
    Space: O(1)
    '''
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) >> 1]


class Solution(object):
    '''算法思想：

    随机从 nums 里边抽取一个数字，那么抽取到 majority 的概率 > 50%，所以可以
    随机抽取一个数字，然后判断其是不是 majority 就可以了

    Time: O(n)
    Space: O(1)
    '''
    def majorityElement(self, nums):
        import random

        n = len(nums)
        mid = (n >> 1) + (n & 1)

        while 1:
            count, index = 0, random.randint(0, n - 1)
            for i in nums:
                count += i == nums[index]
                if count >= mid:
                    return i


class Solution(object):
    '''算法思路：

    Moore Voting Algorithm

    Time: O(n)
    '''
    def majorityElement(self, nums):
        count, majority = 0, None
        for v in nums:
            if not count:
                majority = v
            elif v == majority:
                count += 1
            else:
                count -= 1
        return majority


class Solution(object):
    '''算法思路：

    如果 majority 的第 n 位 为1，那么 nums 里边对应的每个数的第 n 位1的个数的和
    >= mid

    在 c 语言里边这种写法是OK的，但是在Python里边，这种写法不可以，因为在python里边
    负数的符号位是无限向左延伸的，因此需要对最后的结果处理一下

    Time: O(n)
    '''
    def majorityElement(self, nums):
        n, r = len(nums) >> 1, 0
        for i in xrange(32):
            mask = 1 << i
            if len(filter(None, [num & mask for num in nums])) > n:
                r |= mask

        MAX = (1 << 31) - 1
        return (r & MAX) - MAX - 1 if r > MAX else r


s = Solution()
print s.majorityElement([-2147483647])
