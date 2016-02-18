# -*- coding: utf-8 -*-

'''
Binary Search Tree Iterator
===========================

Implement an iterator over a binary search tree (BST). Your iterator will be
initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h)
memory, where h is the height of the tree.
'''


class BSTIterator(object):
    '''算法思路：

    中序遍历
    '''
    def __init__(self, root):
        self.root = root
        self.stack = []

    def hasNext(self):
        return bool(self.root or self.stack)

    def next(self):
        while self.root or self.stack:
            if self.root:
                self.stack.append(self.root)
                self.root = self.root.left
            else:
                poped = self.stack.pop()
                self.root, r = poped.right, poped.val
                break
        return r
