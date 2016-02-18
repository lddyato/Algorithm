# -*- coding: utf-8 -*-

'''
Implement strStr()
==================

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
'''


class Solution(object):
    '''方法思路：

    内置方法
    '''
    def strStr(self, haystack, needle):
        return haystack.find(needle)


class Solution(object):
    '''方法思路：

    一个一个比较
    '''
    def strStr(self, haystack, needle):
        n, m = map(len, (haystack, needle))
        for i in xrange(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1


class Solution(object):
    '''算法思路：

    KMP 算法
    '''
    def getNext(self, substr):
        next, j = [0] * len(substr), -1

        for i, char in enumerate(substr):
            while j >= 0 and substr[j + 1] != substr[i]:
                j = next[j]

            if i > 0 and substr[j + 1] == substr[i]:
                j += 1

            next[i] = j
        return next

    def strStr(self, haystack, needle):
        if not needle:
            return 0

        next, j, m = self.getNext(needle), -1, len(needle)

        for i, char in enumerate(haystack):
            while j >= 0 and needle[j + 1] != char:
                j = next[j]

            if needle[j + 1] == char:
                j += 1

            if j == m - 1:
                return i - j

        return -1
