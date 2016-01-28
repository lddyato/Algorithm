# -*- coding: utf-8 -*-

'''
Binary Tree Paths
=================

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:

["1->2->5", "1->3"]
'''


class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        return ['{}->{}'.format(root.val, p)
                for subtree in (root.left, root.right) if subtree
                for p in self.binaryTreePaths(subtree)]


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)

a.left = b
a.right = c
b.right = d

s = Solution()
print s.binaryTreePaths(a)
