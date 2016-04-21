# -*- coding: utf-8 -*-

'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''


class Solution(object):
    '''算法思路：

    利用slice切片
    '''
    def reverseString(self, s):
        return s[::-1]


class Solution(object):
    '''算法思路：

    动手写
    '''
    def reverseString(self, s):
        s, n = list(s), len(s)
        low, high = 0, n - 1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        return ''.join(s)
