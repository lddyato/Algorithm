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
    '''算法思路：

    模拟加法运算
    '''
    def addBinary(self, a, b):
        a, b = map(int, a), map(int, b)

        i, j, r, mask = len(a) - 1, len(b) - 1, [], 0
        while i >= 0 or j >= 0:
            x = a[i] if i >= 0 else 0
            y = b[j] if j >= 0 else 0

            mask, val = divmod(x + y + mask, 2)
            r.append(val)

            i -= 1
            j -= 1

        if mask:
            r.append(mask)

        return ''.join(map(str, r[::-1]))


s = Solution()
print s.addBinary('100', '0')
