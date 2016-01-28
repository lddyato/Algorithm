# -*- coding: utf-8 -*-

'''
Repeated DNA Sequences
======================

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that
occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:

["AAAAACCCCC", "CCCCCAAAAA"].
'''


class Solution(object):
    '''算法思路：

    用哈希表记录已经存在的 substring，然后判断是否在哈希表里边即可
    '''
    def findRepeatedDnaSequences(self, s):
        r, record = set(), set()
        for i in xrange(len(s) - 9):
            substring = s[i:i + 10]
            [record, r][substring in record].add(substring)
        return list(r)


s  = Solution()
print s.findRepeatedDnaSequences("AAAAAAAAAAA")
