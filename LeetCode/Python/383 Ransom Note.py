# -*- coding: utf-8 -*-

"""
Ransom Note
===========

Given an arbitrary ransom note string and another string containing letters
from all the magazines, write a function that will return true if the ransom 
note can be constructed from the magazines; otherwise, it will return false.  

Each letter in the magazine string can only be used once in your ransom note.

Note:
    You may assume that both strings contain only lowercase letters.

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
"""

import collections


class Solution(object):
    """算法思路：

    统计一下两者的每个字母出现的次数，然后比较，如果ransomNote中的字母不在
    magazine中或者出现的次数比magazine中的多，返回False
    """
    def canConstruct(self, ransomNote, magazine):
        magazineCnt = collections.Counter(magazine)
        noteCnt = collections.Counter(ransomNote)

        for k, v in noteCnt.items():
            if k not in magazineCnt or v > magazineCnt[k]:
                return False
        return True


s = Solution()
print s.canConstruct("a", "b")
