# -*- coding: utf-8 -*-

"""
单源有向图最短路径dijkstra
==========================

用哈希表dis表示源点vertex到各个点的距离，首先要初始化dis，dis[vertex] = 0，
然后再从graph[vertex]中获取相关节点的距离，其余为无穷大。

notVisited表示未访问顶点集合，每次我们从notVisited集合中找到离vertex最近的那个
顶点u，把u从notVisited中去除，然后对于graph[u]中的每个邻接点v重新计算dis[v]，
使得dis[v] = min(dis[v], div[u] + graph[u][v])。如此这样循环，直到notVisited
集合为空。最终dis即为从vertex到各个顶点的最小距离。
"""

import collections


def dijkstra(graph, vertex):
    dis = collections.defaultdict(dict)

    for key in graph:
        dis[key] = graph[vertex].get(key, float("inf"))
    dis[vertex] = 0

    notVisited = set(graph.keys()) - set([vertex])

    while notVisited:
        minDis, u = float("inf"), None
        for v in notVisited:
            if dis[v] < minDis:
                minDis = dis[v]
                u = v

        notVisited.discard(u)

        for v in graph[u]:
            dis[v] = min(dis[v], dis[u] + graph[u][v])

    return dis


graph = {
    "A": {"D": 7, "B": 2, "F": 8},
    "B": {"A": 2, "C": 12},
    "C": {"B": 12, "F": 1, "E": 4},
    "D": {"A": 7, "E": 2},
    "E": {"C": 4, "D": 2, "F": 6},
    "F": {"A": 8, "C": 1, "E": 6}
}

print dijkstra(graph, "A")
