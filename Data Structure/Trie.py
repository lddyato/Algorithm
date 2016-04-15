# -*- coding: utf-8 -*-
# @Author: Lime
# @Date:   2016-04-15 16:20:10
# @Last Modified by:   Lime
# @Last Modified time: 2016-04-15 16:26:14


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
