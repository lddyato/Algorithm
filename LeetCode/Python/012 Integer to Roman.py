# -*- coding: utf-8 -*-

'''
Integer to Roman
================

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution(object):
    def intToRoman(self, num):
        values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        chars = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX',
                 'V', 'IV', 'I')

        i, r = 0, ''
        while i < len(values):
            div, num = divmod(num, values[i])
            r += chars[i] * div
            i += 1
        return r


s = Solution()
print s.intToRoman(1)
