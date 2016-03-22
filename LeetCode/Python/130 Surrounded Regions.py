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


class UnionFind(object):
    def __init__(self, n):
        self.id = range(n)
        self.size = [1] * n
        self.surrounded = [True] * n

    def find(self, label):
        while self.id[label] != label:
            self.id[label] = label = self.id[self.id[label]]
        return label

    def union(self, p, q):
        pId, qId = map(self.find, (p, q))
        if pId == qId:
            return

        less, more = (
            pId, qId) if self.size[pId] < self.size[qId] else (qId, pId)

        self.id[less] = self.id[more]
        self.size[more] += self.size[less]
        self.surrounded[more] &= self.surrounded[less]


class Solution(object):
    '''算法思路：

    并查集，并且记录每个连通集是否是被包围
    '''
    def genIndex(self, i, j, n):
        return i * n + j

    def solve(self, board):
        m, n = len(board), len(board[0]) if board else 0
        unionFind = UnionFind(m * n)

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == 'X':
                    continue

                p = self.genIndex(i, j, n)
                unionFind.surrounded[unionFind.find(p)] &= not (
                    i == 0 or i == m - 1 or j == 0 or j == n - 1)

                for x, y in ((0, -1), (-1, 0)):
                    ii, jj = i + x, j + y
                    q = self.genIndex(ii, jj, n)

                    if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == 'O':
                        unionFind.union(p, q)

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == 'O' and unionFind.surrounded[
                        unionFind.find(self.genIndex(i, j, n))]:
                    row[j] = 'X'


s = Solution()
print s.solve([
    'X X X X'.split(' '),
    'X O O X'.split(' '),
    'X X O X'.split(' '),
    'X O X X'.split(' ')
])
