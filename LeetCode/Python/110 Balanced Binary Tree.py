# -*- coding: utf-8 -*-

'''
Balanced Binary Tree
====================

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.
'''


class Solution(object):
    '''算法思路：

    后序遍历

    分别递归找到左右子树的高度，然后比较是否最多相差 1，然后返回该节点的高度
    '''
    def search(self, root):
        if not self.balanced or not root:
            return 0

        left = self.search(root.left)
        right = self.search(root.right)

        if abs(left - right) > 1:
            self.balanced = False

        return max(left, right) + 1

    def isBalanced(self, root):
        self.balanced = True
        self.search(root)
        return self.balanced
