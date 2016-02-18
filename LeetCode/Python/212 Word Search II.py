# -*- coding: utf-8 -*-

'''
Word Search II
==============

Given a 2D board and a list of words from the dictionary, find all words in the
board.

Each word must be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Return ["eat","oath"].

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''


class TrieNode(object):
    def __init__(self):
        self.word = None
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TrieNode())
        root.word = word


class Solution(object):
    '''算法思路：

    Trie + DFS
    '''
    def search(self, i, j, root, board, m, n, r):
        char = board[i][j]
        if not (char and char in root.children):
            return

        board[i][j], root = None, root.children[char]

        if root.word:
            r.append(root.word)
            root.word = None

        for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ii, jj = i + x, j + y
            if 0 <= ii < m and 0 <= jj < n:
                self.search(ii, jj, root, board, m, n, r)

        board[i][j] = char

    def findWords(self, board, words):
        if not board:
            return []

        tree = Trie()
        [tree.insert(word) for word in words]

        m, n, r = len(board), len(board[0]), []

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                self.search(i, j, tree.root, board, m, n, r)
        return r


board = map(list, ["aaaa", "aaaa","aaaa"])
words = ["aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaab"]

s = Solution()
print s.findWords(board, words)
