# -*- coding: utf-8 -*-

'''
Number of Islands
=================

Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid
are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3
'''


class UnionFind(object):
    '''算法思路：

    并查集
    '''
    def __init__(self, grid):
        self.cols = len(grid[0])
        self.size = [1] * (len(grid) * self.cols)
        self.id = [
            self.genIndex(i, j) if num == '1' else None
            for i, row in enumerate(grid)
            for j, num in enumerate(row)
        ]
        self.count = len(filter(lambda x: x is not None, self.id))

    def genIndex(self, i, j):
        return i * self.cols + j

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

        self.count -= 1


class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        uf = UnionFind(grid)

        [uf.union(uf.genIndex(i, j), uf.genIndex(y, z))
         for i, row in enumerate(grid)
         for j, num in enumerate(row)
         for x, y, z in [(i, i - 1, j), (j, i, j - 1)]
         if num == '1' and x > 0 and grid[y][z] == '1']

        return uf.count


s = Solution()
print s.numIslands([
    '111',
    '010',
    '111'
])
