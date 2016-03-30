# -*- coding: utf-8 -*-

'''
Roman to Integer
================

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution(object):
    '''算法思路：

    从维基百科得到罗马数字的表示方式 https://en.wikipedia.org/wiki/Roman_numerals

    只有 I, X, C 可以作为前缀
    '''
    def romanToInt(self, s):
        maps = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        combines = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        specials = {'I', 'X', 'C'}

        r, i, n = 0, 0, len(s)
        while i < n:
            if s[i] in specials and s[i:i + 2] in combines:
                r += combines[s[i:i + 2]]
                i += 2
            else:
                r += maps[s[i]]
                i += 1
        return r



s = Solution()
print s.romanToInt('MMMCMXCIX')
