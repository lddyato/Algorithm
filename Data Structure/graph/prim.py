# -*- coding: utf-8 -*-

"""
无向图最小生成树Prim算法
=======================

新建一个空的生成树，首先随机从图中任意选择一个顶点，将其放入到空的生成树中。
然后每次从剩下的顶点中找出到生成树所有节点最短的那一条边，放入到生成树中，
如此循环直到所有的顶点都在生成树中。
"""

import collections


def prim(graph):
    """算法思路：

    比较朴素的实现，每次遍历所有跟生成树中有关的节点，然后添加到生成树中

    Time: (VE) V为顶点个数，E为边的个数
    """
    tree = collections.defaultdict(dict)
    tree[graph.keys()[0]] = {}

    cost = 0

    while len(tree) < len(graph):
        minEdge, oldVertex, newVertex = float("inf"), None, None
        for u in tree:
            for v in graph[u]:
                if v not in tree and graph[u][v] < minEdge:
                    minEdge = graph[u][v]
                    oldVertex, newVertex = u, v

        tree[oldVertex][newVertex] = minEdge
        tree[newVertex][oldVertex] = minEdge

        cost += minEdge

    return tree, cost


graph = {
    "A": {"D": 7, "B": 2, "F": 8},
    "B": {"A": 2, "C": 12},
    "C": {"B": 12, "F": 1, "E": 4},
    "D": {"A": 7, "E": 2},
    "E": {"C": 4, "D": 2, "F": 6},
    "F": {"A": 8, "C": 1, "E": 6}
}

print prim(graph)
