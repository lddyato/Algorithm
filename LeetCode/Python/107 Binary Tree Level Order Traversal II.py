# -*- coding: utf-8 -*-

'''
Binary Tree Level Order Traversal II
====================================

Given a binary tree, return the bottom-up level order traversal of its nodes'
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''


class Solution(object):
    '''算法思路：

    BFS
    '''
    def levelOrderBottom(self, root):
        if not root:
            return []

        r = [[root]]
        while r[-1]:
            r.append([
                child for node in r[-1]
                for child in (node.left, node.right) if child
            ])

        return [map(lambda n: n.val, item) for item in r[:-1]][::-1]
