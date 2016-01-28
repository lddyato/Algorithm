# -*- coding: utf-8 -*-

'''
Word Break II
=============

Given a string s and a dictionary of words dict, add spaces in s to construct
a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''


class TrieNode(object):
    def __init__(self, char=None):
        self.char = char
        self.isWord = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.cache = {}

    def insert(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
        root.isWord = True

    def cache(f):
        def method(obj, s):
            if s not in obj.cache:
                obj.cache[s] = f(obj, s)
            return obj.cache[s]
        return method

    @cache
    def breakWord(self, s):
        root, r = self.root, []
        for i, char in enumerate(s):
            if char not in root.children:
                return r

            if root.children[char].isWord:
                r += [
                    [s[:i + 1]] + p
                    for p in (self.breakWord(s[i + 1:]) if s[i + 1:] else [[]])
                ]

            root = root.children[char]
        return r


class Solution(object):
    '''算法思路：

    同 Word Break，在匹配的过程中，找到所有的的字串
    '''
    def wordBreak(self, s, wordDict):
        trie = Trie()
        [trie.insert(word) for word in wordDict]

        return [' '.join(words) for words in trie.breakWord(s)]


class Solution(object):
    '''算法思路：

    不再用前缀树，而是直接匹配，需要注意的一点是，当切割后的后半部分为空时，不应该再
    递归，而是直接处理，要和不存在切割的情况区分开

    结果：AC
    '''
    def cache(f):
        def method(obj, s, wordDict):
            if s not in obj.cache:
                obj.cache[s] = f(obj, s, wordDict)
            return obj.cache[s]
        return method

    @cache
    def find(self, s, wordDict):
        r = []
        for word in wordDict:
            if s.startswith(word):
                sublist = self.find(
                    s[len(word):], wordDict) if s[len(word):] else [[]]
                r += [[word] + p for p in sublist]
        return r

    def wordBreak(self, s, wordDict):
        self.cache = {}
        return map(' '.join, self.find(s, wordDict))


s = Solution()
print s.wordBreak("bb",
["a","b","bbb","bbbb"])
