# -*- coding: utf-8 -*-

'''
Binary Tree Maximum Path Sum
============================

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path does
not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3

Return 6.
'''


class Solution(object):
    '''算法思路：

    后序遍历，返回经过 root 的不拐弯的最大 sum，中间记录最值
    '''
    def search(self, root):
        if not root:
            return 0

        # leetcode 上面这样写会出现错误
        # left, right = map(self.search, (root.left, root.right))
        left, right = self.search(root.left), self.search(root.right)

        m = max(root.val, left + root.val, right + root.val)
        self.r = max([
            self.r, m, left + right + root.val
        ] + ([left] if root.left else []) + ([right] if root.right else []))

        return m

    def maxPathSum(self, root):
        self.r = float('-inf')
        self.search(root)
        return self.r


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}, left: {}, right: {}>'.format(
            self.val, self.left.val if self.left else None,
            self.right.val if self.right else None)


import collections


class Solution(object):
    '''算法思路：

    迭代版本
    '''
    def maxPathSum(self, root):
        stack, color, record, r = [], collections.defaultdict(int), {}, float('-inf')

        while stack or root:
            if root and color[root] < 1:
                stack.append(root)
                root = root.left
            elif color[stack[-1]] < 1:
                color[stack[-1]] += 1
                root = stack[-1].right
            else:
                node = stack.pop()
                color[node] += 1

                left, right = [
                    record.get(c, 0) for c in (node.left, node.right)]

                m = max(node.val, left + node.val, right + node.val)
                r = max([r, m, left + right + node.val] + sum([
                        [record[c]] if c else []
                        for c in (node.left, node.right)
                    ], []))

                record[node] = m

                if stack:
                    color[stack[-1]] += 1
                    root = stack[-1].right
                else:
                    root = None
        return r


a = TreeNode(7)
b = TreeNode(5)
c = TreeNode(3)
d = TreeNode(2)
e = TreeNode(1)

a.left = b
a.right = c
c.left = d
c.right = e


s = Solution()
print s.maxPathSum(a)
