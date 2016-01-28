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
        record, count, longest = {}, 0, 0

        for i, char in enumerate(s):
            if len(record) < 2 or char in record:
                record[char] = i
                count += 1
                continue

            longest = max(count, longest)
            far, close = [
                k for k, v in sorted(record.items(), key=lambda x: x[1])]

            record[close] = i - 1
            count = i - record[far]
            record[char] = i

            del record[far]

        return max(count, longest)


s = Solution()
print s.lengthOfLongestSubstringTwoDistinct("aaa")
