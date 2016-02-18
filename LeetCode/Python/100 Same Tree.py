# -*- coding: utf-8 -*-

'''
Same Tree
=========

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and
the nodes have the same value.
'''


class Solution(object):
    '''算法思路：

    DFS，有一个全局变量表示是否为 same，相当于剪枝
    '''
    def search(self, p, q):
        if not self.same or not p and not q:
            return

        if p and not q or not p and q or p.val != q.val:
            self.same = False
            return

        self.search(p.left, q.left)
        self.search(p.right, q.right)

    def isSameTree(self, p, q):
        self.same = True
        self.search(p, q)
        return self.same


class Solution(object):
    '''算法思路：

    DFS
    '''
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(
            p.left, q.left) and self.isSameTree(p.right, q.right)
