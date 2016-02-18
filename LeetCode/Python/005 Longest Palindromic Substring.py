# -*- coding: utf-8 -*-

'''
Longest Palindromic Substring
=============================

Given a string S, find the longest palindromic substring in S. You may assume
that the maximum length of S is 1000, and there exists one unique longest
palindromic substring.
'''


class Solution(object):
    '''算法思路：

    以每个字符为中心(分奇偶), 向两边搜索，找到最长回文字串

    Time: O(n^2)

    结果：勉强 AC
    '''
    def longestPalindrome(self, s):
        maxLength, odd, index = 0, None, None
        for i in xrange(len(s)):
            # 回文子串长度为奇数时
            r = 0
            while i - r >= 0 and i + r < len(s) and s[i - r] == s[i + r]:
                r += 1

            if 2 * r - 1 > maxLength:
                maxLength = 2 * r - 1
                index = i

            # 回文子串长度为偶数时
            r = 0
            while (i - r >= 0 and i + 1 + r < len(s) and
                    s[i - r] == s[i + 1 + r]):
                r += 1

            if 2 * r > maxLength:
                maxLength = 2 * r
                index = i

        half = maxLength >> 1
        return s[index + (not (maxLength & 1)) - half: index + 1 + half]



class Solution(object):
    '''算法思路：

    Manacher’s algorithm

    其思路是从上面演变而来的.

    s 每个字符两边安插一个 '#' 字符，这样就统一了奇偶，p[i] 表示以 s[i] 为中心的最长
    回文字串的半径，maxReach 表示当前背景下回文字串能够达右边界，idx 为 maxReach
    所对应的回文子串的中心.

    添加 idx 和 maxReach 这两个变量最重要的作用是，利用对称性来减小运算量.

    如果当前 i < maxReach，则需要看其对 idx 的对称节点 2 * idx - i，若对称节点的半径
    小于 maxReach - i，那么就说明 p[i] 一定等于其对称节点的值，因为当前所在的字串是
    对称的。如果对称节点的半径超过了 maxReach - i， 那么 p[i] 至少为 maxReach - i。
    其余情况不确定，必须一一匹配。

    p[i] = min(p[2 * idx - i], maxReach - i) if maxReach > i else 1

    http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html

    Time: O(n)
    '''
    def longestPalindrome(self, s):
        s, n = '#{}#'.format('#'.join(list(s))), len(s) * 2 + 1
        p, idx, maxReach = [0] * n, 0, 0

        for i in xrange(len(s)):
            p[i] = min(p[2 * idx - i], maxReach - i) if maxReach > i else 1

            while i - p[i] >= 0 and i + p[i] < n and s[i + p[i]] == s[i - p[i]]:
                p[i] += 1

            if i + p[i] > maxReach:
                idx = i
                maxReach = i + p[i]

        length = max(p)
        index = p.index(length)

        return ''.join(filter(
            lambda c: c != '#', s[index - length + 1: index + length]))


s = Solution()
print s.longestPalindrome('aabaaa')
