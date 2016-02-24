# -*- coding: utf-8 -*-

'''
Longest Substring with At Most Two Distinct Characters
======================================================

Given a string, find the length of the longest substring T that contains at
most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.
'''


class Solution(object):
    '''算法思路：

    用两个指针保存两个值的最后出现的 index
    '''
    def lengthOfLongestSubstringTwoDistinct(self, s):
        first, second, start, r = [None, None], [None, None], 0, 0
        for i, char in enumerate(s):
            if char != first[0] and char != second[0]:
                if not first[0]:
                    first = [char, i]
                elif not second[0]:
                    second = [char, i]
                else:
                    start, first, second = first[1] + 1, second, [char, i]
            elif char == first[0]:
                first[1] = i
                if second[0]:
                    first, second = second, first
            else:
                second[1] = i

            r = max(r, i - start + 1)
        return r


import collections


class Solution(object):
    '''算法思路：

    更加一般的思路，求最多 k 个不同的字符，用有序字典保存每个字符最后出现的位置，并且
    最后出现的位置是递增的，当 queue 的长度大于 k 的时候，把子串起点挪到 queue 头部
    节点位置的下一位
    '''
    def lengthOfLongestSubstringTwoDistinct(self, s):
        queue, start, r, k = collections.OrderedDict(), 0, 0, 2

        for i, char in enumerate(s):
            if char in queue:
                queue.pop(char)
            queue[char] = i

            if len(queue) > k:
                start = queue.popitem(False)[1] + 1
            r = max(r, i - start + 1)
        return r


s = Solution()
print s.lengthOfLongestSubstringTwoDistinct("aaa")
