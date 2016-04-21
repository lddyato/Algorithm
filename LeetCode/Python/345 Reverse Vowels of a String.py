# -*- coding: utf-8 -*-

'''
Write a function that takes a string as input and reverse only the vowels of a
string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''


class Solution(object):
    '''算法思路：

    Two pointer
    '''
    def reverseVowels(self, s):
        s, n, vowels = list(s), len(s), {'a', 'e', 'i', 'o', 'u'}

        low, high = 0, n - 1
        while low < high:
            while low < n and s[low].lower() not in vowels:
                low += 1
            while high >= 0 and s[high].lower() not in vowels:
                high -= 1
            if low >= high:
                break
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        return ''.join(s)
