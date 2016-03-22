# -*- coding: utf-8 -*-

'''
Find Median from Data Stream
============================

Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

Examples:
[2,3,4] , the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

- void addNum(int num) - Add a integer number from the data stream to the data
  structure.
- double findMedian() - Return the median of all elements so far.

For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
'''


class RedBlackTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1
        self.isRed = True


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def sizeOf(self, node):
        return node.size if node else 0

    @property
    def size(self):
        return self.sizeOf(self.root)

    def rotateLeft(self, root):
        right = root.right

        root.size, right.size = self.sizeOf(
            root.left) + self.sizeOf(right.left) + 1, root.size

        root.right = right.left
        right.left = root

        right.isRed = root.isRed
        root.isRed = True

        return right

    def rotateRight(self, root):
        left = root.left

        root.size, left.size = self.sizeOf(
            root.right) + self.sizeOf(left.right) + 1, root.size

        root.left = left.right
        left.right = root

        left.isRed = root.isRed
        root.isRed = True

        return left

    def flipColor(self, root):
        root.left.isRed = False
        root.right.isRed = False
        root.isRed = True
        return root

    def insertTo(self, root, val):
        if not root:
            return RedBlackTreeNode(val)

        if val > root.val:
            root.right = self.insertTo(root.right, val)
        else:
            root.left = self.insertTo(root.left, val)

        if (root.right and root.right.isRed) and not (
                root.left and root.left.isRed):
            root = self.rotateLeft(root)

        if (root.left and root.left.isRed) and (
                root.left.left and root.left.left.isRed):
            root = self.rotateRight(root)

        if (root.left and root.left.isRed) and (
                root.right and root.right.isRed):
            root = self.flipColor(root)

        root.size = sum(map(self.sizeOf, (root.left, root.right))) + 1
        return root

    def insert(self, val):
        self.root = self.insertTo(self.root, val)
        self.root.isRed = False

    def searchK(self, k, root=None):
        root = root or self.root

        size = self.sizeOf(root.left) + 1
        if k == size:
            return root.val

        return self.searchK(k, root.left) if k < size else self.searchK(
            k - size, root.right)


class MedianFinder(object):
    '''算法思路：

    红黑树

    addNum: O(log(n))
    findMedian: O(log(n))

    结果：勉强 AC
    '''
    def __init__(self):
        self.tree = RedBlackTree()

    def addNum(self, num):
        self.tree.insert(num)

    def findMedian(self):
        size = self.tree.size
        if size & 1:
            return self.tree.searchK(size + 1 >> 1)
        return sum(map(self.tree.searchK, (size >> 1, size + 2 >> 1))) / 2.0


'============================================================================'


import random


class TreapNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1
        self.priority = random.random()


class Treap(object):
    def __init__(self):
        self.root = None

    def sizeOf(self, node):
        return node.size if node else 0

    @property
    def size(self):
        return self.sizeOf(self.root)

    def rotateLeft(self, root):
        right = root.right

        root.size, right.size = self.sizeOf(
            root.left) + self.sizeOf(right.left) + 1, root.size

        root.right = right.left
        right.left = root
        return right

    def rotateRight(self, root):
        left = root.left

        root.size, left.size = self.sizeOf(
            root.right) + self.sizeOf(left.right) + 1, root.size

        root.left = left.right
        left.right = root
        return left

    def insertTo(self, root, val):
        if not root:
            return TreapNode(val)

        if val > root.val:
            root.right = self.insertTo(root.right, val)
            if root.right.priority < root.priority:
                root = self.rotateLeft(root)
        else:
            root.left = self.insertTo(root.left, val)
            if root.left.priority < root.priority:
                root = self.rotateRight(root)

        root.size = sum(map(self.sizeOf, (root.left, root.right))) + 1
        return root

    def insert(self, val):
        self.root = self.insertTo(self.root, val)

    def searchK(self, k, root=None):
        root = root or self.root

        size = self.sizeOf(root.left) + 1
        if k == size:
            return root.val

        return self.searchK(k, root.left) if k < size else self.searchK(
            k - size, root.right)


class MedianFinder(object):
    '''算法思路：

    Treap

    addNum: O(log(n))
    findMedian: O(log(n))

    结果：TLE

    猜测是 Treap 并不像 RedBlackTree 那样严格的保持平衡
    '''
    def __init__(self):
        self.tree = Treap()

    def addNum(self, num):
        self.tree.insert(num)

    def findMedian(self):
        size = self.tree.size
        if size & 1:
            return self.tree.searchK(size + 1 >> 1)
        return sum(map(self.tree.searchK, (size >> 1, size + 2 >> 1))) / 2.0


'============================================================================'


import heapq


class MedianFinder(object):
    '''算法思路：

    用两个 Heap 分别保存最小和最大的部分，因为我们并不需要维护除了中间两个位置外其他数
    的顺序，可以在这个地方做优化

    addNum: O(log(n))
    findMedian: O(1)
    '''
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        maxHeap, minHeap = self.maxHeap, self.minHeap

        heapq.heappush(minHeap, num)
        if len(minHeap) > len(maxHeap):
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))

        if minHeap and minHeap[0] < -maxHeap[0]:
            min, max = minHeap[0], -maxHeap[0]
            heapq.heappushpop(maxHeap, -min)
            heapq.heappushpop(minHeap, max)

    def findMedian(self):
        m, n = map(len, (self.maxHeap, self.minHeap))
        return (-self.maxHeap[0] + (
            self.minHeap[0] if m == n else -self.maxHeap[0])) / 2.0


# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
addNum = mf.addNum
findMedian = mf.findMedian

print addNum(1),findMedian(),addNum(2),findMedian(),addNum(3),findMedian(),addNum(4),findMedian(),addNum(5),findMedian(),addNum(6),findMedian(),addNum(7),findMedian(),addNum(8),findMedian(),addNum(9),findMedian(),addNum(10),findMedian()
