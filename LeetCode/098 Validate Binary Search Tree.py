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
    def traverse(self, root):
        if not (root.left or root.right):
            return True, root.val, root.val

        rMin, rMax = float('inf'), float('-inf')

        if root.left:
            isValid, minimum, maximum = self.traverse(root.left)

            if not isValid or maximum >= root.val:
                return False, 0, 0

            rMin, rMax = min(rMin, minimum), max(rMax, root.val)

        if root.right:
            isValid, minimum, maximum = self.traverse(root.right)

            if not isValid or minimum <= root.val:
                return False, 0, 0

            rMin, rMax = min(rMin, root.val), max(rMax, maximum)

        return True, rMin, rMax

    def isValidBST(self, root):
        if not root:
            return True

        r, _, _ = self.traverse(root)
        return r
