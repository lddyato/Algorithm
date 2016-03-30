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
    result = ['1']

    def say(self, str):
        i, n, r = 0, len(str), []
        while i < n:
            j = i + 1
            while j < n and str[i] == str[j]:
                j += 1
            r.append('{}{}'.format(j - i, str[i]))
            i = j
        return ''.join(r)

    def countAndSay(self, n):
        '''算法思路：

        把每次中间计算的结果缓存起来，这样能够加快 test case
        '''
        for i in range(len(self.result), n):
            self.result.append(self.say(self.result[-1]))
        return self.result[-1]


s = Solution()
print s.countAndSay(6)
