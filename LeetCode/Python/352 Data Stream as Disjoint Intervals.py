#!/usr/bin/env python
# encoding: utf-8

"""
Data Stream as Disjoint Intervals
=================================

Given a data stream input of non-negative integers a1, a2, ..., an, ...,
summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ...,
then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]

Follow up:

What if there are lots of merges and the number of disjoint intervals are
small compared to the data stream's size?
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "<Interval start: {}, end: {}>".format(self.start, self.end)


class BinaryTreeNode(object):
    def __init__(self, minVal, maxVal):
        self.minVal = minVal
        self.maxVal = maxVal
        self.left = None
        self.right = None
        self.full = True


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insertTo(self, root, val):
        if not root:
            return BinaryTreeNode(val, val)

        if root.minVal < val < root.maxVal and not root.full:
            if val < root.right.minVal - 1:
                root.left = self.insertTo(root.left, val)
            else:
                root.right = self.insertTo(root.right, val)

        elif val < root.minVal:
            if val + 1 == root.minVal:
                if root.left:
                    root.left = self.insertTo(root.left, val)
                root.minVal = val
            else:
                newRoot = BinaryTreeNode(val, root.maxVal)
                newRoot.left = BinaryTreeNode(val, val)
                newRoot.right = root

                root = newRoot

        elif val > root.maxVal:
            if val - 1 == root.maxVal:
                if root.right:
                    root.right = self.insertTo(root.right, val)
                root.maxVal = val
            else:
                newRoot = BinaryTreeNode(root.minVal, val)
                newRoot.left = root
                newRoot.right = BinaryTreeNode(val, val)

                root = newRoot

        if (root.left and root.left.full and root.right.full and
                root.left.maxVal + 1 == root.right.minVal):
            root.left = root.right = None
            root.full = True

        if root.left or root.right:
            root.full = False

        return root

    def insert(self, val):
        self.root = self.insertTo(self.root, val)

    def getLeafs(self):
        r, stack, root = [], [], self.root
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if not root.right:
                    if r and root.minVal == r[-1].end + 1:
                        r[-1].end = root.maxVal
                    else:
                        r.append(Interval(root.minVal, root.maxVal))
                root = root.right
        return r


class SummaryRanges(object):
    """算法思路：

    区间树，每个节点维护区间最值，然后根据情况更新节点，非平衡二叉树

    addNum: O(log(n))
    getIntervals: O(n)

    结果：TLE
    """
    def __init__(self):
        self.tree = BinaryTree()

    def addNum(self, val):
        self.tree.insert(val)

    def getIntervals(self):
        return self.tree.getLeafs()


# ====================================================================


import random


class TreapNode(object):
    def __init__(self, key):
        self.key = key
        self.val = Interval(key, key)
        self.priority = random.random()
        self.left = None
        self.right = None

    def __repr__(self):
        return "<TreapNode key: {}, val: {}, priority: {}>".format(
            self.key, self.val, self.priority)


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

    def find(self, key):
        root = self.root
        while root:
            if root.val.start <= key <= root.val.end:
                return root

            if key < root.key:
                root = root.left
            else:
                root = root.right

    def insertTo(self, root, key):
        if not root:
            return TreapNode(key)

        if key < root.key:
            root.left = self.insertTo(root.left, key)
            if root.left.priority < root.priority:
                root = self.rotateRight(root)
        else:
            if root.val.start <= key <= root.val.end:
                return root

            if key == root.val.end + 1:
                root.val.end += 1
                return root

            root.right = self.insertTo(root.right, key)
            if root.right.priority < root.priority:
                root = self.rotateLeft(root)

        return root

    def insert(self, key):
        self.root = self.insertTo(self.root, key)

        rightNode = self.find(key + 1)
        if rightNode:
            leftNode = self.find(key)
            leftNode.val.end = rightNode.val.end
            self.remove(rightNode.key)

    def removeFrom(self, root, key):
        if not root:
            return

        if key < root.key:
            root.left = self.removeFrom(root.left, key)

        elif key > root.key:
            root.right = self.removeFrom(root.right, key)

        elif not (root.left or root.right):
            return

        elif (not root.right or root.left and root.right and
              root.left.priority < root.right.priority):
            root = self.rotateRight(root)
            root.right = self.removeFrom(root.right, key)

        else:
            root = self.rotateLeft(root)
            root.left = self.removeFrom(root.left, key)

        return root

    def remove(self, key):
        self.root = self.removeFrom(self.root, key)

    def traverse(self):
        root, r, stack = self.root, [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                r.append(root.val)
                root = root.right
        return r


class SummaryRanges(object):
    """算法思路：

    平衡二叉树：Treap, key值是每个区间的最小值

    addNum: O(logn)
    getIntervals: O(n)

    结果：TLE
    """
    def __init__(self):
        self.tree = Treap()

    def addNum(self, val):
        self.tree.insert(val)

    def getIntervals(self):
        return self.tree.traverse()


# =====================================================================


class SummaryRanges(object):
    """算法思路：

    最朴素的方法，维护一个区间数组，每次二分插入

    addNum: 二分查找是 O(logn), 但是insert是 O(n)，所以最坏 O(n)
    getIntervals: O(1)

    结果：AC
    """
    def __init__(self):
        self.r = []

    def addNum(self, val):
        low, high = 0, len(self.r) - 1
        while low <= high:
            mid = low + high >> 1
            if val < self.r[mid].start:
                high = mid - 1
            else:
                if mid == len(self.r) - 1 or val < self.r[mid + 1].start:
                    if self.r[mid].start <= val <= self.r[mid].end:
                        return

                    if self.r[mid].end + 1 == val:
                        self.r[mid].end += 1
                        if (mid < len(self.r) - 1 and
                                self.r[mid + 1].start == self.r[mid].end + 1):
                            self.r[mid].end = self.r[mid + 1].end
                            del self.r[mid + 1]
                        return

                    if (mid < len(self.r) - 1 and
                            self.r[mid + 1].start == val + 1):
                        self.r[mid + 1].start -= 1
                        return

                    self.r.insert(mid + 1, Interval(val, val))
                    return

                low = mid + 1

        if self.r and self.r[0].start == val + 1:
            self.r[0].start -= 1
        else:
            self.r.insert(0, Interval(val, val))

    def getIntervals(self):
        return self.r


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(8)
obj.addNum(10)
obj.addNum(9)
obj.addNum(2)
obj.addNum(4)
obj.addNum(3)
obj.addNum(11)
obj.addNum(6)
obj.addNum(7)

print obj.getIntervals()
