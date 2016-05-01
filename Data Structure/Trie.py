# -*- coding: utf-8 -*-

'''
Trie 树
======

字典树：https://en.wikipedia.org/wiki/Trie
'''

class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TrieNode())
        root.isWord = True

    def search(self, word):
        root = self.root
        for char in word:
            root = root.children.get(char, None)
            if not root:
                return False
        return root.isWord

    def startswith(self, prefix):
        root = self.root
        for char in prefix:
            root = root.children.get(char, None)
            if not root:
                return False
        return True
