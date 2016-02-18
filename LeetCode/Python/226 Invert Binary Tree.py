# -*- coding: utf-8 -*-

'''
Invert Binary Tree
==================

Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:

This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew),
but you can’t invert a binary tree on a whiteboard so fuck off.
'''


class Solution(object):
    '''算法思路:

    DFS，每访问一个 node，把左右孩子互换
    '''
    def invertTree(self, root):
        if not root:
            return

        root.left, root.right = root.right, root.left
        map(self.invertTree, (root.left, root.right))

        return root
