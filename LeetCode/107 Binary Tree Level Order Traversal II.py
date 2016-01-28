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
    def levelOrderBottom(self, root):
        if not root:
            return []

        queue, result = [root], []
        while queue:
            sublist, levelNum = [], len(queue)

            for i in xrange(levelNum):
                node = queue.pop(0)
                sublist.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(sublist)
        return result[::-1]
