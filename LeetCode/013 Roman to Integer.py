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
    '''
    def romanToInt(self, s):
        maps = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        combins = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        prefixs = ['I', 'X', 'C']

        i, sum = 0, 0
        while i < len(s):
            if s[i] in prefixs and i + 1 < len(s) and s[i] + s[i+1] in combins:
                sum += combins[s[i] + s[i+1]]
                i += 2
                continue

            sum += maps[s[i]]
            i += 1

        return sum


s = Solution()
print s.romanToInt('MMMCMXCIX')
