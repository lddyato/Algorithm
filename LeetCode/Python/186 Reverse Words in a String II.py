# -*- coding: utf-8 -*-

'''
Reverse Words in a String II
============================

Given an input string, reverse the string word by word. A word is defined as a
sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are
always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array
'''


class Solution(object):
    '''算法思路：

    先反转部分，再反转整体
    '''
    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s):
        i, n = 0, len(s)
        while i < n:
            while i < n and s[i] == ' ':
                i += 1

            if i >= n:
                break

            start = i
            while i < n and s[i] != ' ':
                i += 1
            end = i - 1

            self.reverse(s, start, end)

        self.reverse(s, 0, n - 1)


s = Solution()
s.reverseWords([' ', 'a'])
