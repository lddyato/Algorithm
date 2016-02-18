# -*- coding: utf-8 -*-

'''
The Skyline Problem
===================

A city's skyline is the outer contour of the silhouette formed by all the
buildings in that city when viewed from a distance. Now suppose you are given
the locations and height of all the buildings as shown on a cityscape photo
(Figure A), write a program to output the skyline formed by these buildings
collectively (Figure B).

The geometric information of each building is represented by a triplet of
integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and
right edge of the ith building, respectively, and Hi is its height. It is
guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You
may assume all buildings are perfect rectangles grounded on an absolutely flat
surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as:
[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of
[ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key
point is the left endpoint of a horizontal line segment. Note that the last
key point, where the rightmost building ends, is merely used to mark the
termination of the skyline, and always has zero height. Also, the ground in
between any two adjacent buildings should be considered part of the skyline
contour.

For instance, the skyline in Figure B should be represented as:
[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

- The number of buildings in any input list is guaranteed to be in the range
  [0, 10000].
- The input list is already sorted in ascending order by the left x position Li.
- The output list must be sorted by the x position.
- There must be no consecutive horizontal lines of equal height in the output
  skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not
  acceptable; the three lines of height 5 should be merged into one in the
  final output as such: [...[2 3], [4 5], [12 7], ...]
'''


import random


class TreapNode(object):
    def __init__(self, key, val, isSet=False):
        self.key = key
        self.val = {val} if isSet else val
        self.left = None
        self.right = None
        self.priority = random.random()


class Treap(object):
    def __init__(self, isSet=False):
        self.isSet = isSet
        self.root = None
        self.min = None
        self.max = None

    @property
    def isEmpty(self):
        return not self.root

    def minNode(self):
        if not self.root:
            return

        root = self.root
        while root.left:
            root = root.left
        return root

    def maxNode(self):
        if not self.root:
            return

        root = self.root
        while root.right:
            root = root.right
        return root

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

    def insertTo(self, root, key, val):
        replaced = -1
        if not root:
            return TreapNode(key, val, self.isSet), replaced

        if key == root.key:
            if self.isSet:
                root.val.add(val)
            elif val > root.val:
                replaced, root.val = root.val, val
            else:
                replaced = 0
            return root, replaced

        if key < root.key:
            root.left, replaced = self.insertTo(root.left, key, val)
            if root.left.priority < root.priority:
                root = self.rotateRight(root)
        else:
            root.right, replaced = self.insertTo(root.right, key, val)
            if root.right.priority < root.priority:
                root = self.rotateLeft(root)

        return root, replaced

    def insert(self, key, val):
        self.root, replaced = self.insertTo(self.root, key, val)

        if not self.min or key < self.min.key:
            self.min = self.minNode()

        if not self.max or key > self.max.key:
            self.max = self.maxNode()

        return replaced

    def deleteFrom(self, root, key, val=None):
        if not root:
            return

        if key < root.key:
            root.left = self.deleteFrom(root.left, key, val)
        elif key > root.key:
            root.right = self.deleteFrom(root.right, key, val)
        else:
            if self.isSet:
                root.val.discard(val)
                if root.val:
                    return root

            if not (root.left and root.right):
                return root.left or root.right

            if root.left.priority < root.right.priority:
                root = self.rotateRight(root)
                root.right = self.deleteFrom(root.right, key, val)
            else:
                root = self.rotateLeft(root)
                root.left = self.deleteFrom(root.left, key, val)
        return root

    def delete(self, key, val=None):
        self.root = self.deleteFrom(self.root, key, val)
        if self.min and key == self.min.key:
            self.min = self.minNode()

        if self.max and key == self.max.key:
            self.max = self.maxNode()

    @property
    def maxHeight(self):
        return self.max.key if self.max else 0


class Solution(object):
    '''算法思路：

    利用 indexTree 来存储 [Ri, Hi], heightTree 存储 [Hi, Ri].

    如果有多个 Ri，indexTree 存的是最大那个的 Hi， 而 heightTree 则存储所有的
    [Hi, Ri]

    处理策略是，从左往后扫描 buildings: l, r, h = buildings[i]
    - 如果 indexTree 为空，那么直接 append [l, h]，并把 [r, h], [h, r] 分别
      insert 到 indexTree, heightTree

    - 如果 l < indexTree.min.key 并且 h > heightTree.maxHeight，有两种情况，
      - 如果 l == result[-1][0]，说明有多个 left 边界相同，那么更新 result[-1][1]
      - 否则，append [l, h] 到 result 中去

      最后把 [r, h], [h, r] 分别 insert 到 indexTree, heightTree

    - 如果 l == indexTree.min.key，那么首先删除 indexTree.min.key，并且删除掉
      heightTree 对应的 key=indexTree.min.val, val=indexTree.min.key，这时如果
      h > heightTree.maxHeight 并且 h 和结果中的最后一个高度不相等，那么 append
      [l, h] 到结果中，最后把 [r, h], [h, r] 分别 insert 到 indexTree, heightTree

    - 如果 l > indexTree.min.key，那么一直删除 indexTree.min 一直到
      l <= indexTree.min.key, 期间如果删除前 indexTree.min.val 和
      heightTree.maxHeight 相等，删除后 heightTree.maxHeight 和 结果中最后一个高度
      不同，则把删除前的 indexTree.min.key 和删除后的 heightTree.maxHeight append
      到结果中
    '''
    def getSkyline(self, buildings):
        indexTree, heightTree, result, i, n = (
            Treap(), Treap(True), [], 0, len(buildings))

        while i < n or not indexTree.isEmpty:
            l, r, h = buildings[i] if i < n else (float('inf'), 0, 0)

            while not indexTree.isEmpty and l > indexTree.min.key:
                key, val, pre = (
                    indexTree.min.key, indexTree.min.val, heightTree.maxHeight)

                heightTree.delete(val, key)
                indexTree.delete(key)

                if val == pre and heightTree.maxHeight != result[-1][1]:
                    result.append([key, heightTree.maxHeight])

            if i >= n:
                break

            if indexTree.isEmpty:
                result.append([l, h])

            elif l < indexTree.min.key and h > heightTree.maxHeight:
                if l == result[-1][0]:
                    result[-1][1] = h
                else:
                    result.append([l, h])

            elif l == indexTree.min.key:
                heightTree.delete(indexTree.min.val, indexTree.min.key)
                indexTree.delete(indexTree.min.key)

                if h > heightTree.maxHeight and h != result[-1][1]:
                    result.append([l, h])

            replaced = indexTree.insert(r, h)
            if replaced > 0:
                heightTree.delete(replaced, r)

            if replaced:
                heightTree.insert(h, r)

            i += 1
        return result


s = Solution()
print s.getSkyline([[0,3,3],[1,5,3],[2,4,3],[3,7,3]])
