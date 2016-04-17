# -*- coding: utf-8 -*-

'''
Recover Binary Search Tree
==========================

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a
constant space solution?
'''


class Solution(object):
    '''算法思路：

    中序遍历，然后从序列里边找到两个被 swapped 的点，这里题意其实有点模糊，应该明确的
    说明是 swap 了值

    Space：O(n)
    '''
    def recoverTree(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                r.append(root)
                root = root.right

        one, two = None, None
        for i in xrange(1, len(r)):
            if r[i].val < r[i - 1].val:
                one, two = one or r[i - 1], r[i]
        one.val, two.val = two.val, one.val


class Solution(object):
    '''算法思路：

    同上，只不过再遍历的过程中寻找两个节点

    Space: O(1)
    '''
    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        if root.val < self.pre.val:
            self.first = self.first or self.pre
            self.second = root

        self.pre = root
        self.dfs(root.right)

    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.pre = TreeNode(float('-inf'))

        self.dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
