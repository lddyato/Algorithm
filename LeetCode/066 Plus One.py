# -*- coding: utf-8 -*-

'''
Plus One
========

Given a non-negative number represented as an array of digits, plus one to the
number.

The digits are stored such that the most significant digit is at the head of
the list.
'''


class Solution(object):
    def plusOne(self, digits):
        i, div = len(digits) - 1, 1
        while i >= 0:
            div, digits[i] = divmod(digits[i] + div, 10)
            if not div:
                break
            i -= 1

        if div:
            digits.insert(0, div)

        return digits


s = Solution()
print s.plusOne([0, 1])
