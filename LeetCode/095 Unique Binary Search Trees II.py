# -*- coding: utf-8 -*-

'''
Unique Binary Search Trees II
=============================

Given n, generate all structurally unique BST's (binary search trees) that
store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    '''算法思路：

    生成每一个子树的 BST
    '''
    def generate(self, start, end):
        if start > end:
            return []

        if start == end:
            return [TreeNode(start)]

        if start + 1 == end:
            root1 = TreeNode(start)
            root1.right = TreeNode(end)

            root2 = TreeNode(end)
            root2.left = TreeNode(start)

            return [root1, root2]

        r = []
        for i in xrange(start, end + 1):
            leftTrees = self.generate(start, i - 1)
            rightTrees = self.generate(i + 1, end)

            for lt in leftTrees or [None]:
                for rt in rightTrees or [None]:
                    root = TreeNode(i)
                    root.left, root.right = lt, rt
                    r.append(root)
        return r

    def generateTrees(self, n):
        return self.generate(1, n)
