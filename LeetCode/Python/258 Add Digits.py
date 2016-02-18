# -*- coding: utf-8 -*-

'''
Add Digits
==========

Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''


class Solution(object):
    '''算法思路：

    普通做法，依次计算即可
    '''
    def addDigits(self, num):
        if num < 10:
            return num

        s = 0
        while num > 0:
            num, mod = divmod(num, 10)
            s += mod

        return self.addDigits(s)


class Solution(object):
    '''算法思路：

    观察得到结论
    '''
    def addDigits(self, num):
        return num if num == 0 else num % 9 or 9
