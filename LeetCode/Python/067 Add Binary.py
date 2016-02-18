# -*- coding: utf-8 -*-

'''
Add Binary
==========

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''


class Solution(object):
    def addBinary(self, a, b):
        i, j, div, result = len(a) - 1, len(b) - 1, 0, ''
        while i >= 0 or j >= 0:
            x, y = int(a[i]) if i >= 0 else 0, int(b[j]) if j >= 0 else 0
            div, mod = divmod(x + y + div, 2)

            result = str(mod) + result

            i -= 1
            j -= 1

        if div:
            result = str(div) + result

        return result


s = Solution()
print s.addBinary('100', '0')
