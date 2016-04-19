# -*- coding: utf-8 -*-


class RedBlackTreeNode(object):
    def __init__(self, key):
        self.key = key
        self.isRed = True
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

    def insertTo(self, root, key):
        if not root:
            return RedBlackTreeNode(key)

        if key < root.key:
            root.left = self.insertTo(root.left, key)
        else:
            root.right = self.insertTo(root.right, key)

        if root.right and root.right.isRed and (
                not root.left or not root.left.isRed):
            root = self.rotateLeft(root)

        if (root.left and root.isRed and root.left.left and
                root.left.left.isRed):
            root = self.rotateRight(root)

        if root.left and root.left.isRed and root.right and root.right.isRed:
            root.left.isRed = root.right.isRed = False
            root.isRed = True

        return root

    def insert(self, key):
        self.root = self.insertTo(self.root, key)

    def find(self, key):
        root = self.root
        while root and root.key != key:
            root = root.left if key < root.key else root.right
        return root

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
    for key in range(10):
        tree.insert(key)

    tree.traverse()
