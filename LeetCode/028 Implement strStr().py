# -*- coding: utf-8 -*-

'''
Implement strStr()
==================

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
'''


class Solution(object):
    '''算法思路：

    依次比较
    '''
    def strStr(self, haystack, needle):
        p = 0
        while p < len(haystack) - len(needle) + 1:
            i, j = p, 0
            while j < len(needle):
                if needle[j] != haystack[i]:
                    break
                i += 1
                j += 1
            else:
                return p
            p += 1
        return -1
