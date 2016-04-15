# -*- coding: utf-8 -*-

'''
Word Break
==========

Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''


class TrieNode(object):
    def __init__(self, char=None, isWord=False):
        self.char = char
        self.isWord = isWord
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
    def search(self, s):
        root = self.root
        for i, char in enumerate(s):
            if char not in root.children:
                return False

            if root.children[char].isWord:
                if self.search(s[i + 1:]):
                    return True
            root = root.children[char]
        return root.isWord


class Solution(object):
    '''算法思路：

    可以用 trie
    '''
    def wordBreak(self, s, wordDict):
        trie = Trie()
        [trie.insert(word) for word in wordDict]

        return trie.search(s)

# ===================================================================

def cache(f):
    def method(obj, s, wordDict):
        if s not in obj.cache:
            obj.cache[s] = f(obj, s, wordDict)
        return obj.cache[s]
    return method


class Solution(object):
    '''算法思路：

    记忆化搜索, DFS + cache
    '''
    def __init__(self):
        self.cache = {}

    @cache
    def wordBreak(self, s, wordDict):
        if not s:
            return True

        prefix = ''
        for i, char in enumerate(s):
            prefix += char
            if prefix in wordDict and self.wordBreak(s[i + 1:], wordDict):
                return True
        return False


class Solution(object):
    '''算法思路：

    动态规划, dp[i] 表示前 i 个字符是不是可以用字典中的词来表示
    '''
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [True] + [False] * n

        for i in range(n):
            for j in range(i, -1, -1):
                if s[j:i + 1] in wordDict and dp[j]:
                    dp[i + 1] = True
                    break
        return dp[-1]


s = Solution()

print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
