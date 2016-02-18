# -*- coding: utf-8 -*-

'''
Valid Parentheses
=================

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
'''


class Solution(object):
    def isValid(self, s):
        lefts, rights = ('(', '{', '['), (')', '}', ']')
        maps = dict(zip(lefts, rights))

        stacks = []
        for char in s:
            if char in lefts:
                stacks.append(char)
            else:
                if not stacks or maps[stacks[-1]] != char:
                    return False

                del stacks[-1]

        if stacks:
            return False

        return True


s = Solution()
print s.isValid('({}')
