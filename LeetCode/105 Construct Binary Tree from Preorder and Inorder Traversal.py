# -*- coding: utf-8 -*-

'''
Construct Binary Tree from Preorder and Inorder Traversal
=========================================================

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''


class Solution(object):
    '''算法思路：

    各个部分相对应

    结果：Memory Limit Exceeded
    '''
    def buildTree(self, preorder, inorder):
        if not preorder:
            return

        root, i = TreeNode(preorder[0]), inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root


class Solution(object):
    '''算法思路：

    同上，只不过改成 pointer
    '''
    def build(self, inorder, inStart, inEnd, preorder, preStart):
        if inStart > inEnd:
            return

        root, i = TreeNode(preorder[preStart]), self.r[preorder[preStart]]

        root.left = self.build(inorder, inStart, i - 1, preorder, preStart + 1)
        root.right = self.build(
            inorder, i + 1, inEnd, preorder, preStart + i - inStart + 1)

        return root

    def buildTree(self, preorder, inorder):
        self.r = {v: i for i, v in enumerate(inorder)}
        return self.build(inorder, 0, len(inorder) - 1, preorder, 0)
