# -*- coding: utf-8 -*-

'''
Flatten Binary Tree to Linked List
==================================

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''


class Solution(object):
    '''算法思路：

    先序遍历，然后把遍历结果构成 Linked List
    '''
    def flatten(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                r.append(root)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right

        tail = None
        for i in xrange(len(r) - 1, -1, -1):
            r[i].left, r[i].right, tail = None, tail, r[i]
