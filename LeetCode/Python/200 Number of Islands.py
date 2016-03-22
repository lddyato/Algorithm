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
    def __init__(self, n):
        self.id = range(n)
        self.size = [1] * n
        self.count = n

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
        self.size[more] = self.size[less]
        self.count -= 1


class Solution(object):
    '''算法思路：

    并查集
    '''
    def genIndex(self, i, j, n):
        return i * n + j

    def numIslands(self, grid):
        m, n, count = len(grid), len(grid[0]) if grid else 0, 0
        unionFind = UnionFind(m * n)

        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                p = self.genIndex(i, j, n)

                if char == '0':
                    count += 1
                    continue

                for x, y in ((0, -1), (-1, 0)):
                    ii, jj = i + x, j + y

                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '1':
                        unionFind.union(p, self.genIndex(ii, jj, n))

        return unionFind.count - count


s = Solution()
print s.numIslands([
    '111',
    '010',
    '111'
])
