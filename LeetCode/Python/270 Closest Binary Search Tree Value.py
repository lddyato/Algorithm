# -*- coding: utf-8 -*-

'''
Closest Binary Search Tree Value
================================

Given a non-empty binary search tree and a target value, find the value in
the BST that is closest to the target.

Note:

- Given target value is a floating point.

- You are guaranteed to have only one unique value in the BST that is closest
  to the target.
'''


class Solution(object):
    def closestValue(self, root, target):
        closest = root.val

        while root:
            if abs(target - root.val) < abs(target - closest):
                closest = root.val
            root = root.left if target <= root.val else root.right

        return closest

