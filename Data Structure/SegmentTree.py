# -*- coding: utf-8 -*-

'''
线段树
=====

- 一般用来处理和区间相关的问题，比如 区间极值, 区间统计
- 一般生成后树结构不会变动，不适合用来处理使树结构发生变动的问题
- 线段树是一种结构，要根据不同的问题，添加并维护额外的数据
- insert、query 操作均为 O(log(n))

下面用最大值为例来说明
'''


class SegmentTreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.max = None  # field related with the problem


class SegmentTree(object):
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build(0, len(nums) - 1)

    def build(self, start, end):
        root = SegmentTreeNode(start, end)
        if start == end:
            root.max = self.nums[start]
            return root

        mid = start + end >> 1

        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)

        root.max = max(root.left.max, root.right.max)
        return root

    def modify(self, root, index, val):
        if root.start == root.end == index:
            root.max = val
            return

        if index <= root.left.end:
            self.modify(root.left, index, val)
        else:
            self.modify(root.right, index, val)

        root.max = max(root.left.max, root.right.max)
        return root

    def query(self, root, start, end):
        if not root or start > root.end or end < root.start:
            return float('-inf')

        if start <= root.start and end >= root.end:
            return root.max

        return max(
            self.query(root.left, start, end),
            self.query(root.right, start, end)
        )


if __name__ == '__main__':
    import random

    nums = [random.randint(0, 10000) for _ in xrange(100)]

    tree = SegmentTree(nums)
    root = tree.root

    assert tree.query(root, 0, 100) == tree.query(root, -100, 200) == max(nums)
    assert tree.query(root, 30, 50) == max(nums[30:51])

    tree.modify(root, 40, 1000000000)
    assert tree.query(root, 0, 100) == tree.query(root, -100, 200) == 1000000000
    assert tree.query(root, 30, 50) == 1000000000
