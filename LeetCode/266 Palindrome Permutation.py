# -*- coding: utf-8 -*-

'''
Palindrome Permutation
======================

Given a string, determine if a permutation of the string could form a
palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
'''


class Solution(object):
    '''算法思路：

    能够组合成回文数的条件是 相同字符个数为奇数的个数不超过 1
    '''
    def canPermutePalindrome(self, s):
        maps = {}
        for c in s:
            maps[c] = maps.setdefault(c, 0) + 1

        count = 0
        for v in maps.values():
            if v % 2 != 0:
                count += 1
                if count > 1:
                    return False
        return True


s = Solution()
print s.canPermutePalindrome('code')
print s.canPermutePalindrome('aab')
print s.canPermutePalindrome('carerac')
