# -*- coding: utf-8 -*-

'''
Isomorphic Strings
==================

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''


class Solution(object):
    '''算法思路：

    一一对应
    '''
    def isIsomorphic(self, s, t):
        recordKey, recordValue = {}, {}
        for i in xrange(len(s)):
            if s[i] not in recordKey:
                if t[i] in recordValue:
                    return False
                recordKey[s[i]], recordValue[t[i]] = t[i], s[i]

            elif recordKey[s[i]] != t[i]:
                return False

        return True


class Solution(object):
    def isIsomorphic(self, s, t):
        return len(set(zip(s, t))) ) == len(set(s)) == len(set(t))


class Solution(object):
    '''算法思路：

    可以转换成 s 和 t 分别对index 的映射
    '''
    def isIsomorphic(self, s, t):
        return map(s.find, s) == map(t.find, t)


s = Solution()
print s.isIsomorphic('ab', 'ca')
