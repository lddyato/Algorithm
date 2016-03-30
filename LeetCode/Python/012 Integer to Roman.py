# -*- coding: utf-8 -*-

'''
Integer to Roman
================

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution(object):
    '''算法思路：

    按单位从大到小，依次过滤
    '''
    def intToRoman(self, num):
        units = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                 (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
                 (5, 'V'), (4, 'IV'), (1, 'I')]

        r, pointer = [], 0
        while num > 0:
            while units[pointer][0] > num:
                pointer += 1

            times, num = divmod(num, units[pointer][0])
            r.append(units[pointer][1] * times)

        return ''.join(r)


s = Solution()
print s.intToRoman(1)
