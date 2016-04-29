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
    def __init__(self, words):
        self.root = TrieNode()
        self.build(words)

    def build(self, words):
        for word in words:
            self.insert(word)

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TrieNode())
        root.word = word


class Solution(object):
    '''算法思路：

    Trie + DFS
    '''
    def dfs(self, board, i, j, m, n, root):
        if root.word:
            self.r.append(''.join(root.word))
            root.word = None

        char, board[i][j] = board[i][j], None
        for x, y in ((0, 1), (-1, 0), (0, -1), (1, 0)):
            ii, jj = i + x, j + y
            if 0 <= ii < m and 0 <= jj < n and board[ii][jj] in root.children:
                self.dfs(board, ii, jj, m, n, root.children[board[ii][jj]])
        board[i][j] = char

    def findWords(self, board, words):
        self.r, trie = [], Trie(words)
        m, n = map(len, (board, board[0]))

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char in trie.root.children:
                    self.dfs(board, i, j, m, n, trie.root.children[char])
        return self.r


board = map(list, ["aaaa", "aaaa","aaaa"])
words = ["aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaab"]

s = Solution()
print s.findWords(board, words)
