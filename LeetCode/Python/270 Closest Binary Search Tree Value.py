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
        r = root.val
        while root:
            if abs(root.val - target) < abs(r - target):
                r = root.val
            root = root.left if target < root.val else root.right
        return r
