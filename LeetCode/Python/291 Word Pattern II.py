# -*- coding: utf-8 -*-

'''
Word Pattern II
===============

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty substring in str.

Examples:

pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.

Notes:
You may assume both pattern and str contains only lowercase letters.
'''


class Solution(object):
    '''算法思路：

    同 I，只是用了 tracebacking，有点疑惑的是，OJ 上不能写成这样的形式：

        def wordPatternMatch(self, pattern, str, {}, {}):
    '''
    def match(self, pattern, str, r1, r2):
        if not (pattern or str):
            return True

        if not pattern and str or pattern and not str:
            return False

        char = pattern[0]
        for j in xrange(len(str)):
            substr = str[:j + 1]
            if char not in r1 and substr not in r2:
                r1[char] = substr
                r2[substr] = char

                if self.match(pattern[1:], str[j + 1:], r1, r2):
                    return True

                del r1[char]
                del r2[substr]

            elif (char in r1 and r1[char] == substr and
                    self.match(pattern[1:], str[j + 1:], r1, r2)):
                return True

        return False

    def wordPatternMatch(self, pattern, str):
        r1, r2 = {}, {}
        return self.match(pattern, str, r1, r2)


s = Solution()
print s.wordPatternMatch('aabb', 'xyzabcxzyabc')
