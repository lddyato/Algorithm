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
        self.size[more] += self.size[less]
        self.count -= 1


class Solution(object):
    '''算法思路：

    并查集
    '''
    def countComponents(self, n, edges):
        unionFind = UnionFind(n)
        for p, q in edges:
            unionFind.union(p, q)
        return unionFind.count


s = Solution()
print s.countComponents(5, [[0, 1], [1, 2]])
