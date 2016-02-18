# -*- coding: utf-8 -*-

'''
Shortest Word Distance II
=========================

This is a follow up of Shortest Word Distance. The only difference is now you
are given the list of words and your method will be called repeatedly many
times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and
implements a method that takes two words word1 and word2 and return the
shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both
in the list.
'''


class WordDistance(object):
    '''算法思路：

    记录每个 word 出现的 index，然后比较 word1 和 word2 出现的所有的位置，以找出
    最小的 distance，这里用二分查找进行优化
    '''
    def __init__(self, words):
        self.length = len(words)
        self.records = {}

        for i, w in enumerate(words):
            self.records.setdefault(w, []).append(i)

    def find(self, nums, n):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if n < nums[mid]:
                if mid > 0 and nums[mid - 1] < n or mid == 0:
                    return mid
                high = mid - 1
            else:
                low = mid + 1

        return low

    def shortest(self, word1, word2):
        l1, l2 = map(self.records.get, (word1, word2))

        less, more = l1, l2
        if len(l1) > len(l2):
            less, more = more, less

        distance = self.length
        for i in less:
            index = self.find(more, i)
            if index == 0:
                distance = min(distance, more[index] - i)
            elif index >= len(more):
                distance = min(distance, i - more[-1])
            else:
                distance = min(distance, i - more[index - 1], more[index] - i)

        return distance


s = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print s.shortest('coding', 'practice')
print s.shortest('makes', 'coding')
