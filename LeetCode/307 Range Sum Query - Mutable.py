# -*- coding: utf-8 -*-

'''
Range Sum Query - Mutable
=========================

Given an integer array nums, find the sum of the elements between indices i
and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i
to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Note:
- The array is only modifiable by the update function.
- You may assume the number of calls to update and sumRange function is
  distributed evenly.
'''


class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class SegmentTree(object):
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build(0, len(nums) - 1)

    def build(self, start, end):
        if start > end:
            return

        if start == end:
            return SegmentTreeNode(self.nums[start], start, end)

        mid = start + end >> 1

        left, right = self.build(start, mid), self.build(mid + 1, end)
        root = SegmentTreeNode(left.val + right.val, start, end)
        root.left, root.right = left, right

        return root

    def update(self, i, val, root=None):
        r = root or self.root

        if i < r.start or i > r.end:
            return r.val

        if r.start == r.end == i:
            r.val = val
            return r.val

        r.val = sum([self.update(i, val, c) for c in (r.left, r.right) if c])
        return r.val

    def sumRange(self, i, j, root=None):
        root = root or self.root
        if i > root.end or j < root.start:
            return 0

        if i <= root.start and j >= root.end:
            return root.val

        return sum([
            self.sumRange(i, j, root) for root in (root.left, root.right)])


class NumArray(object):
    '''算法思路：

    线段树
    '''
    def __init__(self, nums):
        self.tree = SegmentTree(nums)

    def update(self, i, val):
        self.tree.update(i, val)

    def sumRange(self, i, j):
        return self.tree.sumRange(i, j)


'========================================================================'


class BinaryIndexedTree(object):
    def __init__(self, nums):
        self.nums = [0] + nums
        self.sums = [0] * (len(self.nums))
        self.build()

    def build(self):
        for i in xrange(1, len(self.nums)):
            for j in xrange(i - (i & -i) + 1, i + 1):
                self.sums[i] += self.nums[j]

    def update(self, i, val):
        oldVal, self.nums[i] = self.nums[i], val

        while i < len(self.nums):
            self.sums[i] += val - oldVal
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r


class NumArray(object):
    '''算法思路：

    树状数组
    '''
    def __init__(self, nums):
        self.tree = BinaryIndexedTree(nums)

    def update(self, i, val):
        self.tree.update(i + 1, val)

    def sumRange(self, i, j):
        return self.tree.sum(j + 1) - self.tree.sum(i)


s = NumArray([-1])

print s.sumRange(0, 0)
s.update(0, 1)
print s.sumRange(0, 0)
