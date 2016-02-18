# -*- coding: utf-8 -*-

'''
Shortest Palindrome
===================

Given a string S, you are allowed to convert it to a palindrome by adding
characters in front of it. Find and return the shortest palindrome you can
find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".
Given "abcd", return "dcbabcd".
'''


class Solution(object):
    '''算法思路：

    Manacher’s algorithm，从开头开始的最长回文子串，然后把剩下的子串反转后 append
    到 s 的前面
    '''
    def shortestPalindrome(self, s):
        original, s, n = s, '#{}#'.format('#'.join(list(s))),  2 * len(s) + 1
        p, idx, maxReach = [0] * n, 0, 0

        for i in xrange(n):
            p[i] = min(maxReach - i, p[2 * idx - i]) if maxReach > i else 1

            while i - p[i] >= 0 and i + p[i] < n and s[i - p[i]] == s[i + p[i]]:
                p[i] += 1

            if i + p[i] > maxReach:
                idx = i
                maxReach = i + p[i]

        for i in xrange(n - 1, -1, -1):
            if p[i] == i + 1:
                return original[p[i] - 1:][::-1] + original
        return original


s = Solution()
print s.shortestPalindrome('abbacd')
