# -*- coding: utf-8 -*-

'''
Add and Search Word - Data structure design
===========================================

Design a data structure that supports the following two operations:

    void addWord(word)
    bool search(word)

search(word) can search a literal word or a regular expression string
containing only letters a-z or .. A . means it can represent any one letter.

For example:

    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
'''


class TrieNode(object):
    def __init__(self, char=None, isKey=False):
        self.children = [None] * 26
        self.char = char
        self.isKey = isKey


class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()
        self.maps = {chr(i): i - 97 for i in xrange(97, 123)}

    def addWord(self, word):
        root = self.root
        for char in word:
            idx = self.maps[char]
            if root.children[idx] is None:
                root.children[idx] = TrieNode(char)
            root = root.children[idx]
        root.isKey = True

    def search(self, word, root=None):
        root = root or self.root
        for i, char in enumerate(word):
            if char != '.':
                idx = self.maps[char]
                if root.children[idx] is None:
                    return False
                root = root.children[idx]
                continue

            return any(
                self.search(word[i+1:], child)
                for child in root.children if child)

        return root.isKey


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.addWord('app')
wordDictionary.addWord('s')

print wordDictionary.search("a")
