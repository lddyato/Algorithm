# -*- coding: utf-8 -*-

'''
Excel Sheet Column Number
=========================

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding
column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''


class Solution(object):
    def titleToNumber(self, s):
        i, base, r = len(s) - 1, 1, 0
        while i >= 0:
            r += base * (ord(s[i]) - 64)
            base *= 26
            i -= 1
        return r


s = Solution()
print s.titleToNumber('AA')
