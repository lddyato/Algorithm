# -*- coding: utf-8 -*-

"""
Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.

Examples:

    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.

Note: You may assume the string contain only lowercase letters.
"""

import collections


class Solution(object):
    """算法思路：

    利用哈希表进行统计，然后遍历找出结果

    Time: O(n)
    Space: O(n)
    """
    def firstUniqChar(self, s):
        counter = collections.Counter(s)
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        return -1


class Solution(object):
    """算法思路：

    利用了进位的思想，当多于2个时进位到two，要比上述解法快2倍左右

    Time: O(n)
    Space: O(1)
    """
    def firstUniqChar(self, s):
        one, two = 0, 0
        for char in s:
            bit = 1 << (ord(char) - 97)
            if not one & bit:
                if not two & bit:
                    one |= bit
                continue

            one &= ~bit
            two |= bit

        for i, char in enumerate(s):
            bit = 1 << (ord(char) - 97)
            if one & bit:
                return i

        return -1


s = Solution()
print s.firstUniqChar("leetcode")
print s.firstUniqChar("leetlt")
