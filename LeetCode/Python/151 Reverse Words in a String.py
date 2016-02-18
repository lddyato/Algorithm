# -*- coding: utf-8 -*-

'''
Reverse Words in a String
=========================

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
'''


class Solution(object):
    '''算法思想：

    自己动手
    '''
    def reverseWords(self, s):
        r, i = '', len(s) - 1
        while i >= 0:
            flag = False
            while i >= 0 and s[i] == ' ':
                flag = True
                i -= 1

            if flag:
                r += ' '

            if i < 0:
                break

            word = ''
            while i >= 0 and s[i] != ' ':
                word = s[i] + word
                i -= 1

            r += word
        return r.strip(' ')


class Solution(object):
    '''算法思想：

    使用内置函数
    '''
    def reverseWords(self, s):
        return ' '.join(filter(None, s.split(' '))[::-1])


s = Solution()
print s.reverseWords('the sky is blue')
