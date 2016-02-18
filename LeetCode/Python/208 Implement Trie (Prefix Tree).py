# -*- coding: utf-8 -*-

'''
Implement Trie (Prefix Tree)
============================

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''


class TrieNode(object):
    def __init__(self, char=None, isWord=False):
        self.children = [None] * 26
        self.char = char
        self.isWord = isWord


class Trie(object):
    '''算法思路：

    前缀树
    '''
    def __init__(self):
        self.root = TrieNode()
        self.maps = {chr(i): i - 97 for i in xrange(97, 123)}

    def insert(self, word):
        root = self.root
        for char in word:
            idx = self.maps[char]
            if root.children[idx] is None:
                root.children[idx] = TrieNode(char)
            root = root.children[idx]
        root.isWord = True

    def search(self, word):
        root = self.root
        for char in word:
            idx = self.maps[char]
            if root.children[idx] is None:
                return False
            root = root.children[idx]
        return root.isWord

    def startsWith(self, prefix):
        root = self.root
        for char in prefix:
            idx = self.maps[char]
            if root.children[idx] is None:
                return False
            root = root.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
insert = trie.insert
startsWith = trie.startsWith
search = trie.search

print insert("app"),insert("apple"),insert("beer"),insert("add"),insert("jam"),insert("rental"),search("apps"),search("app"),search("ad"),search("applepie"),search("rest"),search("jan"),search("rent"),search("beer"),search("jam"),startsWith("apps"),startsWith("app"),startsWith("ad"),startsWith("applepie"),startsWith("rest"),startsWith("jan"),startsWith("rent"),startsWith("beer"),startsWith("jam")
