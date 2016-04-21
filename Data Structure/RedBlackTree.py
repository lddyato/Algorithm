# -*- coding: utf-8 -*-

'''
红黑树
=====

实现方式为 Left-Leaning Red-Black Tree
'''

class RedBlackTreeNode(object):
    def __init__(self, key, isRed=True):
        self.key = key
        self.isRed = isRed
        self.left = None
        self.right = None

    def __repr__(self):
        return '<RedBlackTreeNode key: {}, isRed: {}>'.format(
            self.key, self.isRed)


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def rotateLeft(self, root):
        right = root.right
        root.right = right.left
        right.left = root

        root.isRed, right.isRed = right.isRed, root.isRed
        return right

    def rotateRight(self, root):
        left = root.left
        root.left = left.right
        left.right = root

        root.isRed, left.isRed = left.isRed, root.isRed
        return left

    def flipColor(self, root):
        root.isRed = not root.isRed
        root.left.isRed = not root.left.isRed
        root.right.isRed = not root.right.isRed

    def fixUp(self, root):
        if root.right and root.right.isRed:
            root = self.rotateLeft(root)

        if (root.left and root.left.isRed and root.left.left and
                root.left.left.isRed):
            root = self.rotateRight(root)

        if root.left and root.left.isRed and root.right and root.right.isRed:
            self.flipColor(root)

        return root

    def insertTo(self, root, key):
        if not root:
            return RedBlackTreeNode(key)

        if key < root.key:
            root.left = self.insertTo(root.left, key)
        else:
            root.right = self.insertTo(root.right, key)

        return self.fixUp(root)

    def insert(self, key):
        self.root = self.insertTo(self.root, key)
        self.root.isRed = False

    def find(self, key):
        root = self.root
        while root and root.key != key:
            root = root.left if key < root.key else root.right
        return root

    def moveRedRight(self, root):
        self.flipColor(root)
        if root.left.left and root.left.left.isRed:
            root = self.rotateRight(root)
            self.flipColor(root)
        return root

    def deleteMax(self, root):
        if root.left and root.left.isRed:
            root = self.rotateRight(root)

        if not root.right:
            return

        if not root.right.isRed and not (
                root.right.left and root.right.left.isRed):
            root = self.moveRedRight(root)

        root.right = self.deleteMax(root.right)
        return self.fixUp(root)

    def moveRedLeft(self, root):
        self.flipColor(root)
        if root.right.left and root.right.left.isRed:
            root.right = self.rotateRight(root.right)
            root = self.rotateLeft(root)
            self.flipColor(root)
        return root

    def deleteMin(self, root):
        if not root.left:
            return

        if not root.left.isRed and not (
                root.left.left and root.left.left.isRed):
            root = self.moveRedLeft(root)

        root.left = self.deleteMin(root.left)
        return self.fixUp(root)

    def deleteFrom(self, root, key):
        if not root:
            return

        if key < root.key:
            if not (root.left and root.left.isRed) and not (
                    root.left and root.left.left and root.left.left.isRed):
                root = self.moveRedLeft(root)
            root.left = self.deleteFrom(root.left, key)
        else:
            if root.left and root.left.isRed:
                root = self.rotateRight(root)

            if key == root.key and not root.right:
                return

            if not (root.right and root.right.isRed) and not (
                    root.right and root.right.left and root.right.left.isRed):
                root = self.moveRedRight(root)

            if key == root.key:
                neighbor = root.right
                while neighbor.left:
                    neighbor = neighbor.left
                root.key = neighbor.key
                root.right = self.deleteMin(root.right)
            else:
                root.right = self.deleteFrom(root.right, key)

        return self.fixUp(root)

    def delete(self, key):
        self.root = self.deleteFrom(self.root, key)
        if self.root:
            self.root.isRed = False

    def traverse(self):
        queue = [self.root]
        while queue:
            print(queue)
            for _ in range(len(queue)):
                node = queue.pop(0)
                if not node:
                    continue
                [queue.append(c) for c in (node.left, node.right)]


if __name__ == '__main__':
    tree = RedBlackTree()
    for key in range(100):
        tree.insert(key)

    tree.traverse()

    for key in range(10):
        tree.delete(key)

    tree.traverse()
