# -*- coding: utf-8 -*-

'''
ZigZag Conversion
=================

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for
better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number
of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''


class Solution(object):
    '''算法思路：

    观察，把每一行保存到一个数组里边
    '''
    def convert(self, s, numRows):
        if numRows < 1:
            return ''

        if numRows == 1:
            return s

        rows, n  = [''] * min(numRows, len(s)), 2 * numRows - 2

        for i, char in enumerate(s):
            mod = i % n
            if mod > n / 2:
                mod = n - mod

            rows[mod] += char

        return ''.join(rows)


s = Solution()
print s.convert('PAYPALISHIRING', 100)
