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


class Solution(object):
    '''算法思路：

    根据题意，要成为一棵树，必须满足以下要求，缺一不可：
      - 无闭环
      - 连通集个数为1
      - 数的边数 e 和节点 n 满足 e = n - 1

    所以一个节点也可以是一棵树

    使用并查集可以解决该类问题
    '''
    def validTree(self, n, edges):
        if not edges:
            return n == 1

        self.id = range(n)
        self.size = [1] * n
        self.record = {}

        for num1, num2 in edges:
            id1, id2 = map(self.find, (num1, num2))

            if num1 in self.record and num2 in self.record and id1 == id2:
                return False

            for num in (num1, num2):
                self.record.setdefault(num, num)

            self.union(id1, id2)

        v = self.find(self.record.keys()[0])
        for k in self.record:
            if self.find(k) != v:
                return False

        return len(self.record) == n

    def find(self, id):
        while id != self.id[id]:
            self.id[id] = self.id[self.id[id]]
            id = self.id[id]
        return id

    def union(self, id1, id2):
        r1, r2 = map(self.find, (id1, id2))
        if r1 == r2:
            return

        less, more = (r1, r2) if self.size[r1] < self.size[r2] else (r2, r1)
        self.id[less] = self.id[more]
        self.size[more] += self.size[less]


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
