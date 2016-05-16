# -*- coding: utf-8 -*-

'''
Excel Sheet Column Title
========================

Given a positive integer, return its corresponding column title as appear in
an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
'''


class Solution(object):
    '''算法思路：

    10 进制转换为 26 进制, 不过需要做一下修改
    '''
    def convertToTitle(self, n):
        r = []
        while n:
            n, mod = divmod(n, 26)
            r.append(chr(64 + (mod if mod else 26)))
            n -= mod == 0
        return ''.join(r[::-1])


s = Solution()
print s.convertToTitle(2345)
