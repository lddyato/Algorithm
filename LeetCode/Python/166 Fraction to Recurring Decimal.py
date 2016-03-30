# -*- coding: utf-8 -*-

'''
Fraction to Recurring Decimal
=============================

Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

- Given numerator = 1, denominator = 2, return "0.5".
- Given numerator = 2, denominator = 1, return "2".
- Given numerator = 2, denominator = 3, return "0.(6)".
'''


import collections


class Solution(object):
    '''算法思路：

    用 hashtable 保存被除数，注意考虑 corner cases
      - 负数
      - 0
    '''
    def fractionToDecimal(self, numerator, denominator):
        record = collections.OrderedDict()
        genStr = lambda l: ''.join(map(str, l))

        sign = '-' if (
            numerator < 0 and denominator > 0 or
            numerator > 0 and denominator < 0) else ''
        numerator, denominator = map(abs, (numerator, denominator))

        div, mod = divmod(numerator, denominator)
        while mod and mod not in record:
            record[mod], mod = divmod(mod * 10, denominator)

        if not record:
            return '{}{}'.format(sign, div)

        if mod not in record:
            return '{}{}.{}'.format(sign, div, genStr(record.values()))

        first, second, flag = [], [], False
        for k, v in record.items():
            if k == mod:
                flag = True

            (second if flag else first).append(v)

        return '{}{}.{}({})'.format(sign, div, genStr(first), genStr(second))


s = Solution()
print s.fractionToDecimal()
