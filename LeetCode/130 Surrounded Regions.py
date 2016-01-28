# -*- coding: utf-8 -*-

'''
Surrounded Regions
==================

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''


import operator


class UnionFind(object):
    '''算法思路：

    并查集，并且记录每个连通集是否是被包围
    '''
    def __init__(self, board):
        self.m = len(board)
        self.n = len(board[0])
        self.length = self.m * self.n

        self.id = [None] * self.length
        self.size = [1] * self.length
        self.surrounded = [True] * self.length

        [operator.setitem(self.id, *([self.genIndex(i, j)] * 2))
         for i, row in enumerate(board)
         for j, val in enumerate(row) if val == 'O']

    def genIndex(self, i, j):
        return self.n * i + j

    def find(self, p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        idp, idq = map(self.find, (p, q))
        if idp == idq:
            return

        less, more = (
            (idp, idq) if self.size[idp] < self.size[idq] else (idq, idp))

        self.id[less] = self.id[more]
        self.size[more] += self.size[less]
        self.surrounded[more] = self.surrounded[less] and self.surrounded[more]


class Solution(object):
    def solve(self, board):
        if not board:
            return

        uf = UnionFind(board)

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val != 'O':
                    continue

                index = uf.genIndex(i, j)

                [uf.union(index, uf.genIndex(y, z))
                 for x, y, z in ((i, i - 1, j), (j, i, j - 1))
                 if x > 0 and board[y][z] == 'O']

                if i == 0 or j == 0 or i == uf.m - 1 or j == uf.n - 1:
                    uf.surrounded[uf.find(index)] = False

        [operator.setitem(board[i], j, 'X')
         for i in xrange(uf.m)
         for j in xrange(uf.n)
         if board[i][j] == 'O' and uf.surrounded[uf.find(uf.genIndex(i, j))]]



s = Solution()
print s.solve([
    'X X X X'.split(' '),
    'X O O X'.split(' '),
    'X X O X'.split(' '),
    'X O X X'.split(' ')
])
