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


class UnionFind(object):
    def __init__(self, n):
        self.id = range(n)
        self.size = [1] * n
        self.count = n

    def find(self, label):
        while self.id[label] != label:
            self.id[label] = label = self.id[self.id[label]]
        return label

    def union(self, p, q):
        pId, qId = map(self.find, (p, q))
        if pId == qId:
            return

        less, more = (
            pId, qId) if self.size[pId] < self.size[qId] else (qId, pId)

        self.id[less] = self.id[more]
        self.size[more] += self.size[less]
        self.count -= 1


class Solution(object):
    '''算法思路：

    并查集
    '''
    def longestConsecutive(self, nums):
        nums = set(nums)
        unionFind, record = UnionFind(len(nums)), {}

        for i, num in enumerate(nums):
            if num - 1 in record:
                unionFind.union(i, record[num - 1])

            if num + 1 in record:
                unionFind.union(i, record[num + 1])

            record[num] = i

        return max(unionFind.size)


class Solution(object):
    '''算法思路：

    用哈希表维护每个连续数列左右两端的信息，即 {num: [left, right, length]}

    复杂度：O(n)
    '''
    def longestConsecutive(self, nums):
        record, r = {}, 0
        for num in set(nums):
            cnt = record.get(
                num - 1, [0] * 3)[-1] + record.get(num + 1, [0] * 3)[-1] + 1

            if num - 1 not in record and num + 1 not in record:
                record[num] = [num, num, cnt]
            elif num - 1 in record and num + 1 in record:
                record[record[num - 1][0]][1:] = [record[num + 1][1], cnt]
                record[record[num + 1][1]][::2] = [record[num - 1][0], cnt]
            elif num - 1 in record:
                record[record[num - 1][0]][1:] = [num, cnt]
                record[num] = [record[num - 1][0], num, cnt]
            else:
                record[record[num + 1][1]][::2] = [num, cnt]
                record[num] = [num, record[num + 1][1], cnt]

            r = max(r, cnt)
        return r


class Solution(object):
    '''算法思路：

    维护一个 {number: length} 的 hash，保证连续的序列最大最小值存储的是正确的 length

    参考了: https://leetcode.com/discuss/67390/my-simple-answer-in-python-real-o-n

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


s = Solution()
print s.longestConsecutive([1, 2, 4, 5, 3])
print s.id
print s.find(4)
