# -*- coding: utf-8 -*-

'''
Scramble String
===============

Given a string s1, we may represent it as a binary tree by partitioning it to
two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two
children.

For example, if we choose the node "gr" and swap its two children, it produces
a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it
produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled
string of s1.
'''


class Solution(object):
    def cache(f):
        def method(obj, s1, s2):
            key = '{}:{}'.format(s1, s2)
            if key not in obj.r:
                obj.r[key] = f(obj, s1, s2)
            return obj.r[key]
        return method

    @cache
    def search(self, s1, s2):
        if s1 == s2:
            return True

        length = len(s1)
        for l in xrange(1, length):
            if self.search(s1[:l], s2[:l]) and self.search(s1[l:], s2[l:]):
                return True

            if self.search(s1[:l], s2[length - l:]) and self.search(
                    s1[l:], s2[:length - l]):
                return True

        return False

    def isScramble(self, s1, s2):
        '''算法思路：

        分治法 + DFS，当左半部分长度分别为 1 到 length - 1 时，递归得到

        s1[:l] - s2[:l] and s1[l:] - s2[l:]，或者
        s1[:l] - s2[length - l:] and s1[l:] - s2[:length - l]

        是不是匹配
        '''
        if len(s1) != len(s2):
            return False

        self.r = {}
        return self.search(s1, s2)


s = Solution()
print s.isScramble("abcdefghijklmn", "efghijklmncadb")
