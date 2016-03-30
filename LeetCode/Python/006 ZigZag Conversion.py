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

    观察可知，具有明显的周期性
    '''
    def convert(self, s, numRows):
        rows = range(numRows) + range(numRows - 2, 0, -1)

        r, i, n = [[] for _ in range(numRows)], 0, len(s)
        while i < n:
            for row in rows:
                if i >= n:
                    break

                r[row].append(s[i])
                i += 1

        return ''.join(map(''.join, r))



s = Solution()
print s.convert('PAYPALISHIRING', 100)
