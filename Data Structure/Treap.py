# -*- coding: utf-8 -*-

'''
Treap
=====

树堆：https://en.wikipedia.org/wiki/Treap
'''

import random


class TreapNode(object):
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreapNode key: {}, priority: {}>'.format(
            self.key, self.priority)


class Treap(object):
    def __init__(self):
        self.root = None

    def rotateLeft(self, root):
        right = root.right
        root.right = right.left
        right.left = root
        return right

    def rotateRight(self, root):
        left = root.left
        root.left = left.right
        left.right = root
        return left

    def _insertTo(self, root, key):
        if not root:
            return TreapNode(key)

        if key < root.key:
            root.left = self._insertTo(root.left, key)
            if root.left.priority < root.priority:
                root = self.rotateRight(root)
        else:
            root.right = self._insertTo(root.right, key)
            if root.right.priority < root.priority:
                root = self.rotateLeft(root)
        return root

    def insert(self, key):
        self.root = self._insertTo(self.root, key)

    def _removeFrom(self, root, key):
        if not root:
            return

        if key < root.key:
            root.left = self._removeFrom(root.left, key)
            return root

        if key > root.key:
            root.right = self._removeFrom(root.right, key)
            return root

        if not (root.left or root.right):
            return

        if (not root.right or root.left and root.right and
                root.left.priority < root.right.priority):
            root = self.rotateRight(root)
            root.right = self._removeFrom(root.right, key)
            return root

        root = self.rotateLeft(root)
        root.left = self._removeFrom(root.left, key)
        return root

    def remove(self, key):
        self.root = self._removeFrom(self.root, key)

    def find(self, key):
        root = self.root
        while root and root.key != key:
            root = root.left if key < root.key else root.right
        return root

    def traverse(self):
        if not self.root:
            return

        queue = [self.root]
        while queue:
            print queue
            for _ in range(len(queue)):
                node = queue.pop(0)
                [queue.append(c) for c in (node.left, node.right) if c]


if __name__ == '__main__':
    treap = Treap()
    for key in range(100):
        treap.insert(key)

    print treap.find(99)

    for key in range(90):
        treap.remove(key)

    treap.traverse()
