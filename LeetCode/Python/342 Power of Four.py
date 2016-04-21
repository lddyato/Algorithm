# -*- coding: utf-8 -*-

'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''


import math


class Solution(object):
    '''算法思路：

    看 logged 是否为整数即可
    '''
    def isPowerOfFour(self, num):
        if num <= 0:
            return False

        logged = math.log(num, 4)
        return abs(round(logged) - logged) < 1e-7
