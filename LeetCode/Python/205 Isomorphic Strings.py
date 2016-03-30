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
        if len(s) != len(t):
            return False

        table1, table2 = {}, {}
        for i, char in enumerate(s):
            if char not in table1 and t[i] not in table2:
                table1[char], table2[t[i]] = t[i], char
            elif not (char in table1 and t[i] in table2 and
                    table1[char] == t[i] and table2[t[i]] == char):
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
