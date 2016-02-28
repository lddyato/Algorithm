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
    '''方法思路：

    brute force

    Time: O(n^2)
    结果：TLE
    '''
    def findRepeatedDnaSequences(self, s):
        r, n = set(), len(s)
        for i in xrange(n - 9):
            substr = s[i:i + 10]
            if substr not in r:
                for j in xrange(i + 1, n - 9):
                    if substr == s[j:j + 10]:
                        r.add(substr)
                        break
        return list(r)


class Solution(object):
    '''算法思路：

    KMP

    Time: O(n^2)
    结果：TLE
    '''
    def getNext(self, substr):
        next, j = [-1] * len(substr), -1
        for i, char in enumerate(substr):
            while j >= 0 and substr[j + 1] != char:
                j = next[j]

            if i and substr[j + 1] == char:
                j += 1

            next[i] = j
        return next

    def search(self, string, substr):
        next, m, j = self.getNext(substr), len(substr), -1
        for i, char in enumerate(string):
            while j >= 0 and substr[j + 1] != char:
                j = next[j]

            if substr[j + 1] == char:
                j += 1

            if j == m - 1:
                return i - j
        return -1

    def findRepeatedDnaSequences(self, s):
        r, n = set(), len(s)
        for i in xrange(n - 9):
            substr = s[i:i + 10]
            if substr not in r and self.search(s[i + 1:], substr) != -1:
                r.add(substr)

        return list(r)


class TrieNode(object):
    def __init__(self, char=None):
        self.char = char
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TrieNode(char))

    def search(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return True


class Solution(object):
    '''算法思路：

    前缀树

    Time: O(n)
    结果：TLE
    '''
    def findRepeatedDnaSequences(self, s):
        trie, r, n = Trie(), set(), len(s)
        for i in xrange(n - 9):
            substr = s[i:i + 10]
            if trie.search(substr):
                r.add(substr)
            else:
                trie.insert(substr)
        return list(r)


class Solution(object):
    '''算法思路：

    用哈希表记录已经存在的 substring，然后判断是否在哈希表里边即可

    Time: O(n)
    结果：AC
    '''
    def findRepeatedDnaSequences(self, s):
        r, record, n = set(), set(), len(s)
        for i in xrange(n - 9):
            substring = s[i:i + 10]
            [record, r][substring in record].add(substring)
        return list(r)


s  = Solution()
print s.findRepeatedDnaSequences("AAAAAAAAAAA")
