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
        base, r = 1, 0
        for char in s[::-1]:
           r += (ord(char) - 64) * base
           base *= 26
        return r


s = Solution()
print s.titleToNumber('AA')
