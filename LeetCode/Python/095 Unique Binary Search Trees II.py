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


def cache(f):
    def method(obj, i, j):
        if not obj.dp[i][j]:
            obj.dp[i][j] = f(obj, i, j)
        return obj.dp[i][j]
    return method


class Solution(object):
    '''算法思路：

    记忆化搜索
    '''
    def generate(self, i, j):
        if i > j:
            return [None]

        if i == j:
            return [TreeNode(i)]

        r = []
        for k in range(i, j + 1):
            for left in self.generate(i, k - 1):
                for right in self.generate(k + 1, j):
                    root = TreeNode(k)
                    root.left, root.right = left, right
                    r.append(root)
        return r

    def generateTrees(self, n):
        if n == 0:
            return []

        self.dp = [[None] * (n + 1) for _ in range(n)]
        return self.generate(1, n)
