# -*- coding: utf-8 -*-

'''
Given two numbers represented as strings, return multiplication of the numbers
as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''


class Solution(object):
    '''算法思路：

    模拟乘法运算
    '''
    def multiply(self, num1, num2):
        matrix, n, m, maxlen = [], len(num1), len(num2), 0
        for i in range(n - 1, -1, -1):
            row, mask = [0] * (n - 1 - i), 0
            for j in range(m - 1, -1, -1):
                mask, val = divmod(int(num1[i]) * int(num2[j]) + mask, 10)
                row.append(val)

            if mask:
                row.append(mask)

            maxlen = max(maxlen, len(row))
            matrix.append(row)

        mask, r = 0, []
        for i in range(maxlen):
            sum = mask
            for row in matrix:
                sum += row[i] if i < len(row) else 0
            mask, val = divmod(sum, 10)
            r.append(val)

        if mask:
            r.append(mask)

        return ''.join(map(str, r[::-1])).lstrip('0') or '0'


s = Solution()
print s.multiply('0', '0')
