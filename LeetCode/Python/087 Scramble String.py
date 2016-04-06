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


def cache(f):
    def method(obj, s1, s2):
        key = '{}:{}'.format(s1, s2)
        if key not in obj.cache:
            obj.cache[key] = f(obj, s1, s2)
        return obj.cache[key]
    return method


class Solution(object):
    '''算法思路：

    分治法 + DFS，当左半部分长度分别为 1 到 length - 1 时，递归得到

    s1[:l] - s2[:l] and s1[l:] - s2[l:]，或者
    s1[:l] - s2[length - l:] and s1[l:] - s2[:length - l]

    是不是匹配
    '''
    def __init__(self):
        self.cache = {}

    @cache
    def isScramble(self, s1, s2):
        if s1 == s2 or s1 == s2[::-1]:
            return True

        n = len(s1)
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i]) and
                    self.isScramble(s1[i:], s2[i:]) or
                    self.isScramble(s1[:i], s2[n - i:]) and
                    self.isScramble(s1[i:], s2[:n - i])):
                return True
        return False


s = Solution()
print s.isScramble("abcdefghijklmn", "efghijklmncadb")
