# -*- coding: utf-8 -*-

'''
Binary Tree Zigzag Level Order Traversal
========================================

Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''


class Solution(object):
    '''算法思路：

    使用双端队列，根据 level 的不同 左右子树压入的顺序和压入首尾不同
    '''
    def zigzagLevelOrder(self, root):
        import collections

        if not root:
            return []

        stack, r, level = collections.deque([root]), [], 1
        while stack:
            row = []
            for _ in xrange(len(stack)):
                pop, append = (
                    (stack.pop, stack.appendleft) if level & 1 else
                    (stack.popleft, stack.append))

                top = pop()
                row.append(top.val)

                [append(c) for c in ((top.left, top.right)
                 if level & 1 else (top.right, top.left)) if c]

            level += 1
            r.append(row)
        return r
