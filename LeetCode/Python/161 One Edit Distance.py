# -*- coding: utf-8 -*-

'''
One Edit Distance
=================

Given two strings S and T, determine if they are both one edit distance apart.
'''


class Solution(object):
    '''算法思路：

    根据不同的情况进行分析：
    - 长度相差大于 1 的，编辑距离肯定大于 1
    - 长度相等的，判断其不相等字符个数是否为 1 即可
    - 长度相差为 1 的，去除掉较长字符串里第一个不相等的字符，判断剩下是否相等即可
    '''
    def isOneEditDistance(self, s, t):
        diff = abs(len(s) - len(t))

        if diff > 1 or s == t:
            return False

        if diff == 0:
            return sum([s[i] != t[i] for i in xrange(len(s))]) == 1

        if len(s) > len(t):
            s, t = t, s

        for i in xrange(len(s)):
            if s[i] != t[i]:
                return s[i:] == t[i+1:]
        return True


s = Solution()
print s.isOneEditDistance('abc', 'ab')
