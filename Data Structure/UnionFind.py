# -*- coding: utf-8 -*-

""" Union Find - Weighted Quick-Union With Path Compression

N nodes labled from 0 to N-1.

Mainly two operations:
  - find: find the group id the node belongs to
  - union: union two group

Two data property:
  - id: the label i's group id
  - size: the label i's group size
"""


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
