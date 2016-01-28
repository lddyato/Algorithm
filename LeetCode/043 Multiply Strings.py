# -*- coding: utf-8 -*-

'''
Given two numbers represented as strings, return multiplication of the numbers
as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''


class Solution(object):
    def multiply(self, num1, num2):
        c2n = lambda char: ord(char) - ord('0')

        len1, len2 = len(num1), len(num2)
        i, r = len2 - 1, [0] * (len1 + len2)
        while i >= 0:
            j, div = len1 - 1, 0
            while j >= 0:
                div, mod = divmod(c2n(num2[i]) * c2n(num1[j]) + div, 10)

                count, start, plus_div = 0, len2 - 1 - i + len1 - 1 - j, mod
                while plus_div:
                    plus_div, r[start + count] = divmod(
                        plus_div + r[start + count], 10)
                    count += 1
                j -= 1

            if div:
                r[start + 1] = r[start + 1] + div
            i -= 1

        return ''.join(map(str, r[::-1])).lstrip('0') or '0'


s = Solution()
print s.multiply('0', '0')
