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


class Solution(object):
    '''算法思路：

    重要的一点是，哈希 key 为分子
    '''
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return 2 ** 31 - 1

        sign = '-' if (
            numerator > 0 and denominator < 0 or
            numerator < 0 and denominator > 0
        ) else ''
        numerator, denominator = map(abs, (numerator, denominator))

        integer, numerator = divmod(numerator, denominator)
        if not numerator:
            return '{}{}'.format(sign, integer)

        makeStr = lambda l: ''.join(map(str, l))

        sequence, hashTable, i = [], {}, 0
        while numerator and numerator not in hashTable:
            hashTable[numerator] = i

            quotient, numerator = divmod(numerator * 10, denominator)
            sequence.append(quotient)

            i += 1

        if not numerator:
            return '{}{}.{}'.format(sign, integer, makeStr(sequence))

        i = hashTable[numerator]
        return '{}{}.{}({})'.format(
            sign, integer, makeStr(sequence[:i]), makeStr(sequence[i:]))


s = Solution()
print s.fractionToDecimal()
