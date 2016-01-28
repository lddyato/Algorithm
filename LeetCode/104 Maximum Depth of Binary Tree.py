# -*- coding: utf-8 -*-

'''
Maximum Depth of Binary Tree
============================

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.
'''


class Solution(object):
    '''算法思路:

    DFS，先序遍历
    '''
    def dfs(self, root, depth=0):
        if not root:
            self.max = max(depth, self.max)
            return

        depth += 1
        self.dfs(root.left, depth)
        self.dfs(root.right, depth)

    def maxDepth(self, root):
        self.max = 0
        self.dfs(root)
        return self.max