# -*- coding: utf-8 -*-

'''
Minimum Depth of Binary Tree
============================

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the
root node down to the nearest leaf node.
'''


class Solution(object):
    '''算法思路：

    DFS
    '''

    def dfs(self, root):
        return min([
            self.dfs(child) for child in (root.left, root.right) if child
        ] or [0]) + 1

    def minDepth(self, root):
        return self.dfs(root) if root else 0


class Solution(object):
    '''算法思路：

    BFS，层序遍历
    '''
    def minDepth(self, root):
        if not root:
            return 0

        queue, level = [root], 1
        while queue:
            for i in xrange(len(queue)):
                node = queue.pop(0)

                if not node.left and not node.right:
                    return level

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1
