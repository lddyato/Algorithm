# -*- coding: utf-8 -*-

'''
Palindrome Partitioning
=======================

Given a string s, partition s such that every substring of the partition is a
palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]

'''


class Solution(object):
    '''算法思路：

    对于每一个回文前缀，计算出剩下的回文数组，然后相加
    '''
    def isPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s):
        return sum([
            [[s[:i+1]] + p for p in self.partition(s[i+1:]) or [[]]]
            for i in xrange(len(s)) if self.isPalindrome(s, 0, i)
        ], [])


s = Solution()
print s.partition('')
