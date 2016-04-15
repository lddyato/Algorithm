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

    递归搜索
    '''
    def maxDepth(self, root):
        if not root:
            return 0

        return max(map(self.maxDepth, (root.left, root.right))) + 1
