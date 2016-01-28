# -*- coding: utf-8 -*-

'''
Number of Islands II
====================

A 2d grid map of m rows and n columns is initially filled with water. We may
perform an addLand operation which turns the water at position (row, col) into
a land. Given a list of positions to operate, count the number of islands after
each addLand operation. An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically. You may assume all four
edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water
and 1 represents land).

0 0 0
0 0 0
0 0 0

Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0

Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0

Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0

Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0

We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the
positions?
'''


class UnionFind(object):
    def __init__(self, m, n, positions):
        self.n = n
        self.size = [0] * (m * n)
        self.id = [None] * (m * n)
        self.count = 0

    def genIndex(self, i, j):
        return self.n * i + j

    def add(self, i, j):
        index = self.genIndex(i, j)

        self.size[index] = 1
        self.id[index] = index
        self.count += 1

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
    '''算法思路：

    典型的并查集
    '''
    def numIslands2(self, m, n, positions):
        uf, r = UnionFind(m, n, positions), []

        for i, j in positions:
            uf.add(i, j)
            index = uf.genIndex(i, j)

            neighbors = zip(
                (j > 0, i > 0, j + 1 < n, i + 1 < m),
                (uf.genIndex(x, y) for x, y in ((i, j - 1), (i - 1, j), (
                    i, j + 1), (i + 1, j)))
            )

            [uf.union(index, neighbor) for condition, neighbor in neighbors
             if condition and uf.id[neighbor] is not None]

            r.append(uf.count)

        return r


s = Solution()
print s.numIslands2(1, 2, [[0, 1], [0, 0]])
