# -*- coding: utf-8 -*-

'''
Letter Combinations of a Phone Number
=====================================

Given a digit string, return all possible letter combinations that the number
could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in
any order you want.
'''


class Solution(object):
    '''算法思路：

    递归
    '''

    maps = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits, i=0):
        if i >= len(digits):
            return []

        return [
            prefix + item
            for prefix in self.maps[ord(digits[i]) - 48]
            for item in self.letterCombinations(digits, i + 1) or ['']
        ]


class Solution(object):
    '''算法思路：

    动态规划
    '''
    maps = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits):
        dp = []
        for char in digits:
            dp = [prefix + candidates for prefix in dp or ['']
                  for candidates in self.maps[ord(char) - 48]]
        return dp


s = Solution()
print s.letterCombinations('1')
