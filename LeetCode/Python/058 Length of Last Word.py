# -*- coding: utf-8 -*-

'''
Length of Last Word
===================

Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

For example,
Given s = "Hello World",
return 5.
'''


class Solution(object):
    '''算法思路：

    split，然后找到最后一个不为空的元素
    '''
    def lengthOfLastWord(self, s):
        s = s.split(' ')
        for i in range(len(s) - 1, -1, -1):
            if s[i]:
                return len(s[i])
        return 0


s = Solution()
print s.lengthOfLastWord(' asd ')
