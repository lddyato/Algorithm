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


class Solution(object):
    '''算法思路：

    用 hashtable 保存已经 clone 的节点，BFS 遍历所有的节点，中间把 cloned 的节点
    连接起来
    '''
    def cloneGraph(self, node):
        if not node:
            return

        graph = UndirectedGraphNode(node.label)
        visited, record, queue = {graph.label}, {graph.label: graph}, [node]

        cloneNode = lambda label: record.setdefault(
            label, UndirectedGraphNode(label))

        for root in queue:
            clonedRoot = cloneNode(root.label)

            for neighbor in root.neighbors:
                clonedRoot.neighbors.append(cloneNode(neighbor.label))

                if neighbor.label not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor.label)

        return graph
