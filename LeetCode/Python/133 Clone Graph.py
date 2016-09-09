# -*- coding: utf-8 -*-

'''
Clone Graph
===========

Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.

OJ's undirected graph serialization:

Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and
each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as
separated by #.

1. First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
2. Second node is labeled as 1. Connect node 1 to node 2.
3. Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming
   a self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
'''


class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


import collections


class Solution(object):
    '''算法思路：

    用 hashtable 保存已经 clone 的节点，BFS 遍历所有的节点，中间把 cloned 的节点
    连接起来
    '''
    def cloneGraph(self, node):
        if not node:
            return

        record = {node.label: UndirectedGraphNode(node.label)}
        queue = collections.deque([node])

        while queue:
            item = queue.popleft()
            for neighbor in item.neighbors:
                if neighbor.label not in record:
                    record[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)

                record[item.label].neighbors.append(record[neighbor.label])

        return record[node.label]


class Solution(object):
    """算法思路：

    同上，不过这次是用DFS
    """
    def dfs(self, node):
        if node.label in self.record:
            return self.record[node.label]

        self.record[node.label] = UndirectedGraphNode(node.label)
        for enighbor in node.neighbors:
            self.record[node.label].neighbors.append(self.dfs(enighbor))

        return self.record[node.label]

    def cloneGraph(self, node):
        if not node:
            return

        self.record = {}
        return self.dfs(node)
