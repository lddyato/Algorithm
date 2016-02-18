# -*- coding: utf-8 -*-

'''
Binary Tree Vertical Order Traversal
====================================

Given a binary tree, return the vertical order traversal of its nodes' values.
(ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to
right.

Examples:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its vertical order traversal as:

[
  [9],
  [3,15],
  [20],
  [7]
]

Given binary tree [3,9,20,4,5,2,7],

    _3_
   /   \
  9    20
 / \   / \
4   5 2   7

return its vertical order traversal as:

[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]
'''


class Solution(object):
    '''算法思路：

    DFS, 首先遍历一下，根据 offset 找到同处于同一列的元素，然后按照 depth 排序
    '''
    def traverse(self, root, offset=0, depth=0):
        if not root:
            return

        self.record.setdefault(offset, []).append([root.val, depth])

        self.traverse(root.left, offset - 1, depth + 1)
        self.traverse(root.right, offset + 1, depth + 1)

    def verticalOrder(self, root):
        if not root:
            return []

        self.record = {}
        self.traverse(root)

        left, right = [f(self.record.keys()) for f in (min, max)]

        r = [self.record[i] for i in xrange(left, right + 1)]
        for i, row in enumerate(r):
            r[i] = map(lambda x: x[0], sorted(row, key=lambda x: x[1]))

        return r


class Solution(object):
    '''算法思路:

    BFS
    '''
    def verticalOrder(self, root):
        import collections

        queue, r = [(root, 0)], collections.defaultdict(list)
        for root, offset in queue:
            if root:
                r[offset].append(root.val)
                queue += [(root.left, offset - 1), (root.right, offset + 1)]

        minOffset, maxOffset = [
            f(r.keys()) for f in (min, max)] if r else [0, -1]

        return [r[i] for i in xrange(minOffset, maxOffset + 1)]
