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
    def letterCombinations(self, digits):
        maps = [
            '', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        if not digits:
            return []

        alphas = maps[int(digits[0])]
        if len(digits) == 1:
            return list(alphas)

        left = self.letterCombinations(digits[1:])
        return [a + s for a in alphas for s in left] if alphas else left


s = Solution()
print s.letterCombinations('1')
