# -*- coding: utf-8 -*-

'''
Given an integer array nums, find the sum of the elements between indices i
and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

- You may assume that the array does not change.
- There are many calls to sumRange function.
'''


class NumArray(object):
    '''算法思路：

    计算前缀和
    '''
    def __init__(self, nums):
        self.sums = [0] * (len(nums) + 1)
        for i, num in enumerate(nums, 1):
            self.sums[i] = self.sums[i - 1] + num

    def sumRange(self, i, j):
        return self.sums[j + 1] - self.sums[i]


'========================================================================'


class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end


class NumArray(object):
    '''算法思路:

    线段树，使用数组实现
    '''
    def __init__(self, nums):
        self.tree = [None] * (4 * len(nums))
        self.build(0, 0, len(nums) - 1, nums)

    def build(self, root, start, end, nums):
        if start > end:
            return

        if start == end:
            self.tree[root] = SegmentTreeNode(nums[start], start, end)
            return

        mid, left, right = start + end >> 1, 2 * root + 1, 2 * root + 2

        self.build(left, start, mid, nums)
        self.build(right, mid + 1, end, nums)

        self.tree[root] = SegmentTreeNode(
            self.tree[left].val + self.tree[right].val, start, end)

    def sumRange(self, i, j, root=0):
        rootNode = self.tree[root]

        if i > rootNode.end or j < rootNode.start:
            return 0

        if i <= rootNode.start and j >= rootNode.end:
            return rootNode.val

        return sum([
            self.sumRange(i, j, root) for root in (root * 2 + 1, root * 2 + 2)])


'========================================================================'


class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class NumArray(object):
    '''算法思路：

    线段树，使用树实现
    '''
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

    def sumRange(self, i, j, root=None):
        root = root or self.root

        if i > root.end or j < root.start:
            return 0

        if i <= root.start and j >= root.end:
            return root.val

        return sum([
            self.sumRange(i, j, root) for root in (root.left, root.right)])


'======================================================================='


class BinaryIndexedTree(object):
    def __init__(self, nums):
        self.nums = [0] + nums
        self.sums = [0] * len(self.nums)
        self.build()

    def build(self):
        for i in xrange(1, len(self.nums)):
            for j in xrange(i + 1 - (i & -i), i + 1):
                self.sums[i] += self.nums[j]

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

    def sumRange(self, i, j):
        return self.tree.sum(j + 1) - self.tree.sum(i)


numarray = NumArray([-2,0,3,-5,2,-1])
print numarray.sumRange(1, 2)
