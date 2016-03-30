# -*- coding: utf-8 -*-

'''
Longest Common Prefix
=====================

Write a function to find the longest common prefix string amongst an array of
strings.
'''


class Solution(object):
    '''算法思路：

    每次前进 1 步，比较每个 str 的相应位的值是否都相等
    '''
    def longestCommonPrefix(self, strs):
        prefix, i = [], 0
        while strs:
            char = None
            for s in strs:
                if i >= len(s) or char is not None and s[i] != char:
                    return ''.join(prefix)

                if char is None:
                    char = s[i]

            i += 1
            prefix.append(char)

        return ''.join(prefix)


s = Solution()
print s.longestCommonPrefix(['abc', 'abd'])
