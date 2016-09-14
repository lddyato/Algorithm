# -*- coding: utf-8 -*-

"""
有向图任意两点最短路径Floyd算法
==============================

利用动态规划思想，dp[i][j] = min(dp[i][k] + dp[k][j])

Time: O(v^3)
"""

import collections


def floyd(graph):
    vertices = graph.keys()
    dp = collections.defaultdict(dict)

    # 初始化所有节点为无穷大
    for u in vertices:
        for v in vertices:
            dp[u][v] = float("inf")

    # 节点自己为0
    for v in vertices:
        dp[v][v] = 0

    # 对于图中两点之间直接距离
    for u in graph:
        for v in graph[u]:
            dp[u][v] = graph[u][v]

    # 动态规划求dp[i][j]
    for k in vertices:
        for i in vertices:
            for j in vertices:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return dp


graph = {
    "A": {"D": 7, "B": 2, "F": 8},
    "B": {"A": 2, "C": 12},
    "C": {"B": 12, "F": 1, "E": 4},
    "D": {"A": 7, "E": 2},
    "E": {"C": 4, "D": 2, "F": 6},
    "F": {"A": 8, "C": 1, "E": 6}
}

print floyd(graph)
