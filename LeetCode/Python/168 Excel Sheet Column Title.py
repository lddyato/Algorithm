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

    10 进制转换为 26 进制
    '''
    def convertToTitle(self, n):
        result = []
        while n:
            n, mod = divmod(n, 26)
            if mod:
                result.append(chr(64 + mod))
            else:
                n -= 1
                result.append('Z')
        return ''.join(result[::-1])


s = Solution()
print s.convertToTitle(2345)
