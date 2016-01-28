# -*- coding: utf-8 -*-

'''
Count and Say
=============

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''


class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return '1'

        s, count, current, r = self.countAndSay(n - 1), 0, None, ''
        for i, char in enumerate(s):
            if i == 0 or i > 0 and char == s[i - 1]:
                count += 1
            else:
                r += str(count) + current
                count = 1

            current = char

        return r + str(count) + current


s = Solution()
print s.countAndSay(6)
