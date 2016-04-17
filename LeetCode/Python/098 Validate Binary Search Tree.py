# -*- coding: utf-8 -*-

'''
Validate Binary Search Tree
===========================

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's
  key.
- The right subtree of a node contains only nodes with keys greater than the
  node's key.
- Both the left and right subtrees must also be binary search trees.
'''


class Solution(object):
    '''算法思路：

    分别递归查看左右结构是否满足定义
    '''
    def dfs(self, root):
        if not root:
            return float('-inf'), float('inf')

        maxL, minL = self.dfs(root.left)
        maxR, minR = self.dfs(root.right)

        if maxL >= root.val or minR <= root.val:
            self.r = False

        return max(maxR, root.val), min(minL, root.val)

    def isValidBST(self, root):
        self.r = True
        self.dfs(root)
        return self.r
