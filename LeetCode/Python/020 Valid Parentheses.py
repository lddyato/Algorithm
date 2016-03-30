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
    '''算法思路；

    因为其是成对出现的，因此用栈
    '''
    def isValid(self, s):
        stack, table = [], {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in {'(', '[', '{'}:
                stack.append(char)
            elif not stack or table[char] != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack


s = Solution()
print s.isValid('({}')
