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
        i, prefix = 0, ''
        while 1:
            char = None
            for s in strs:
                if i >= len(s):
                    return prefix

                char = char or s[i]
                if char != s[i]:
                    return prefix

            if not char:
                break

            prefix += char
            i += 1

        return prefix


s = Solution()
print s.longestCommonPrefix(['abc', 'abd'])
