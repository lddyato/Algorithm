# -*- coding: utf-8 -*-

'''
Graph Valid Tree
================

Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check whether these edges
make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all
edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear
together in edges.
'''


class UnionFind(object):
    '''算法思路：

    根据题意，树是无环连通图，要成为一棵树，必须满足以下要求，缺一不可：
      - 无闭环，即边数 e 和节点 n 满足 e = n - 1
      - 连通集个数为1

    使用并查集可以解决该类问题
    '''
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
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        unionFind = UnionFind(n)
        for p, q in edges:
            unionFind.union(p, q)

        return unionFind.count == 1


s = Solution()
print s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
print s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
print s.validTree(5, [[0, 1], [1, 2], [3, 4]])
print s.validTree(5, [[0, 1], [2, 1]])
print s.validTree(5, [[0, 1], [2, 3], [1, 2]])
print s.validTree(2, [[1, 0]])
print s.validTree(3, [[1, 0]])
print s.validTree(1, [])
print s.validTree(2, [])
