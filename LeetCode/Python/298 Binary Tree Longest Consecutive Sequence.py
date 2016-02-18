# -*- coding: utf-8 -*-

'''
Binary Tree Longest Consecutive Sequence
========================================

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in
the tree along the parent-child connections. The longest consecutive path need
to be from parent to child (cannot be the reverse).

For example,

   1
    \
     3
    / \
   2   4
        \
         5

Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    /
   2
  /
 1

Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
'''


class Solution(object):
    '''算法思路：

    递归求解

    结果：maximum recursion depth exceeded
    '''
    def consecutive(self, root):
        if not root:
            return 0

        left, right = map(self.consecutive, (root.left, root.right))

        leftConsecutive = False
        if not root.left or root.val == root.left.val - 1:
            self.longest = max(self.longest, left + 1)
            leftConsecutive = True

        rightConsecutive = False
        if not root.right or root.val == root.right.val - 1:
            self.longest = max(self.longest, right + 1)
            rightConsecutive = True

        return max(
            [1, left + 1][leftConsecutive],
            [1, right + 1][rightConsecutive])

    def longestConsecutive(self, root):
        self.longest = 0
        self.consecutive(root)
        return self.longest


class Solution(object):
    '''算法思路：

    迭代方式

    结果：AC
    '''
    def longestConsecutive(self, root):
        stack, poped, longest = [], None, 0
        while stack or root:
            if root:
                consecutive = 1
                for p, c in [(poped, 'right'), (stack and stack[-1], 'left')]:
                    if (p and getattr(p[0], c) is root and
                            p[0].val == root.val - 1):
                        consecutive = p[1] + 1

                longest = max(longest, consecutive)
                stack.append([root, consecutive])
                root = root.left
            else:
                poped = stack.pop()
                root = poped[0].right
        return longest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return '<TreeNode {}>'.format(self.val)


a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(2)
d = TreeNode(4)
e = TreeNode(5)

a.right = b
b.left = c
b.right = d
d.right = e

s = Solution()
print s.longestConsecutive(a)
