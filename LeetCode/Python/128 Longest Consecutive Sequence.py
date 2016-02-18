# -*- coding: utf-8 -*-

'''
Longest Consecutive Sequence
============================

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its
length: 4.

Your algorithm should run in O(n) complexity.
'''


class Solution(object):
    '''算法思路：

    先排序，然后遍历找出最长的序列，由于用了 sorted 所以时间复杂度为 O(n logn)
    '''
    def longestConsecutive(self, nums):
        nums, i, m = sorted(set(nums)), 0, 0

        while i < len(nums):
            n = 1
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                n += 1
                i += 1

            m = max(m, n)
            i += 1

        return m


class Solution(object):
    '''算法思路：

    维护一个 {number: length} 的 hash，保证连续的序列最大最小值存储的是正确的 length

    参考: https://leetcode.com/discuss/67390/my-simple-answer-in-python-real-o-n

    复杂度：O(n) 经提交测试，实际上该方法还没有上面方法效率高
    '''
    def longestConsecutive(self, nums):
        maps, max_length = {}, 0

        for n in nums:
            length, left_length, right_length = 1, 0, 0

            if n in maps:
                continue

            maps[n] = length

            if n - 1 in maps:
                left_length = maps[n - 1]
                length += left_length

            if n + 1 in maps:
                right_length = maps[n + 1]
                length += right_length

            maps[n - left_length] = maps[n + right_length] = length
            max_length = max(max_length, length)

        return max_length


class Solution(object):
    '''算法思路：

    利用并查集来处理

    Time: O(n)
    '''
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        length = len(nums)

        self.id = range(length)
        self.size = [1] * length
        self.record = {}

        for i, n in enumerate(nums):
            if n in self.record:
                continue

            if n not in self.record:
                self.record[n] = i

            if n - 1 in self.record:
                self.union(i, self.record[n - 1])

            if n + 1 in self.record:
                self.union(i, self.record[n + 1])

        return max(self.size)

    def find(self, id):
        while id != self.id[id]:
            self.id[id] = self.id[self.id[id]]
            id = self.id[id]

        return id

    def union(self, id1, id2):
        root1, root2 = map(self.find, (id1, id2))
        if root1 == root2:
            return

        less, more = (
            (root1, root2)
            if self.size[root1] < self.size[root2]
            else (root2, root1))

        self.id[less] = self.id[more]
        self.size[more] += self.size[less]


s = Solution()
print s.longestConsecutive([1, 2, 4, 5, 3])
print s.id
print s.find(4)
