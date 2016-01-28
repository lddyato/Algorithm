# -*- coding: utf-8 -*-

'''
Number of Connected Components in an Undirected Graph
=====================================================

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge
is a pair of nodes), write a function to find the number of connected
components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges
are undirected, [0, 1] is the same as [1, 0] and thus will not appear together
in edges.
'''


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.size = [1] * n
        self.id = range(n)

    def find(self, p):
        while self.id[p] != p:
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
    def countComponents(self, n, edges):
        unionFind = UnionFind(n)
        [unionFind.union(*e) for e in edges]
        return unionFind.count


s = Solution()
print s.countComponents(5, [[0, 1], [1, 2]])
