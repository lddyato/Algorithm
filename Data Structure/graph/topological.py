# -*- coding: utf-8 -*-

"""
有向图拓扑排序
=============

基本思路是找到入度为0的顶点，然后把跟该顶点相连的节点的入度减去
【他们之间相连的个数】，然后把该顶点从图中删除。循环该过程，一直到找不到入度
为0的顶点为止。

如果最后图不为空，那么说明存在环，拓扑序列不存在，否则得到一个拓扑序列。我们
可以利用该特性判断一个有向图中是否有环。

一个有向图有可能存在多个拓扑序列。

如何找出所有有向无环图呢？可以利用DFS + 回溯，思想跟上述是一样的。首先找到当
前所有入度为0的顶点，对于每一个顶点，我们首先把跟该顶点相连的节点的入度减去
【他们之间相连的个数】，然后把该顶点从入度集合中删除，然后递归调用DFS，然后
利用回溯法把原来减去的加上，把该顶点再次添加到入度集合中。 DFS结束的条件是，
入度集合为空。这时，我们把path保存起来。
"""

import collections


class TopologicalPath(object):
    """找到任意一条拓扑序列"""

    def __init__(self, vertices, edges):
        self.graph = collections.defaultdict(
            lambda: collections.defaultdict(int)
        )

        self.v = collections.defaultdict(int)
        for vertex in vertices:
            self.v[vertex] = 0

        for from_, to in edges:
            self.graph[from_][to] += 1
            self.v[to] += 1

    def sort(self):
        path = []
        queue = collections.deque([
            vertex for vertex, count in self.v.items() if count == 0
        ])

        while queue:
            vertex = queue.popleft()
            path.append(vertex)

            for to in self.graph[vertex]:
                self.v[to] -= self.graph[vertex][to]
                if self.v[to] == 0:
                    queue.append(to)

            del self.graph[vertex]

        return [] if self.graph else path


class TopologicalCycle(TopologicalPath):
    """判断有向图中是否存在环"""

    def exist(self):
        return bool(self.sort())


class TopologicalPaths(object):
    """找到所有的拓扑排序序列"""

    def __init__(self, vertices, edges):
        self.graph = collections.defaultdict(
            lambda: collections.defaultdict(int)
        )

        self.v = collections.defaultdict(int)
        for vertex in vertices:
            self.v[vertex] = 0

        for from_, to in edges:
            self.graph[from_][to] += 1
            self.v[to] += 1

        self.paths = []

    def dfs(self, path):
        if not self.v:
            self.paths.append(path)
            return

        queue = [vertex for vertex, count in self.v.items() if count == 0]
        for vertex in queue:
            for to in self.graph[vertex]:
                self.v[to] -= self.graph[vertex][to]

            del self.v[vertex]
            self.dfs(path + [vertex])
            self.v[vertex] = 0

            for to in self.graph[vertex]:
                self.v[to] += self.graph[vertex][to]

    def sort(self):
        self.dfs([])
        return self.paths
