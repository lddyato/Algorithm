# -*- coding: utf-8 -*-

'''
Inorder Successor in BST
========================

Given a binary search tree and a node in it, find the in-order successor of
that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
'''


class Solution(object):
    '''算法思路：

    线索二叉树
    '''
    def inorderSuccessor(self, root, p):
        if root is p or p.right:
            p = p.right
            while p and p.left:
                p = p.left
            return p

        while root:
            if not root.left:
                root = root.right
            else:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right

                if pre is p:
                    return root

                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    root = root.right
