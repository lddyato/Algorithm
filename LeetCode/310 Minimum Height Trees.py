# -*- coding: utf-8 -*-

'''
Minimum Height Trees
====================

For a undirected graph with tree characteristics, we can choose any node as the
root. The result graph is then a rooted tree. Among all possible rooted trees,
those with minimum height are called minimum height trees (MHTs). Given such a
graph, write a function to find all the MHTs and return a list of their root
labels.

Format:

The graph contains n nodes which are labeled from 0 to n - 1. You will be given
the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges
are undirected, [0, 1] is the same as [1, 0] and thus will not appear together
in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Note:

(1) According to the definition of tree on Wikipedia: “a tree is an undirected
    graph in which any two vertices are connected by exactly one path. In other
    words, any connected graph without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest downward
    path between the root and a leaf.
'''


import collections


class Solution(object):
    '''算法思路：

    构建树，以每一个节点为根节点从上往下找到最小高度，然后选出最小高度即可

    复杂度：O(n*n)

    结果：TLE
    '''
    def getHeight(self, neighbors, root):
        queue, depth, visited = (
            collections.deque([root]), 1, [0] * len(neighbors))

        while queue:
            for _ in xrange(len(queue)):
                node = queue.popleft()
                visited[node] = 1
                [queue.append(i) for i in neighbors[node] if not visited[i]]
            depth += 1
        return depth

    def findMinHeightTrees(self, n, edges):
        if not edges or len(edges) >= n:
            return []

        neighbors = [[] for _ in xrange(n)]
        [neighbors[i].append(j) for x, y in edges for i, j in ((x, y), (y, x))]

        depths = [
            self.getHeight(neighbors, i)
            for i in xrange(n)
            if len(neighbors[i]) > (1 if len(edges) > 1 else 0)
        ]

        minimum = min(depths)
        return [i for i, depth in enumerate(depths) if depth == minimum]


class Solution(object):
    '''算法思路：

    每次去掉叶子节点，直到剩下的节点个数 <= 2

    结果：AC
    '''
    def findMinHeightTrees(self, n, edges):
        if not edges:
            return [0]

        neighbors = collections.defaultdict(dict)
        for x, y in edges:
            neighbors[x][y] = 1
            neighbors[y][x] = 1

        while len(neighbors) > 2:
            leafs = [node for node in neighbors if len(neighbors[node]) == 1]

            for node in leafs:
                other = neighbors[node].keys()[0]

                del neighbors[node]
                del neighbors[other][node]

        return neighbors.keys()


s = Solution()
print s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
