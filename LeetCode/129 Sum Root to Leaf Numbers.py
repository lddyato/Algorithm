# -*- coding: utf-8 -*-

'''
Sum Root to Leaf Numbers
========================

Given a binary tree containing digits from 0-9 only, each root-to-leaf path
could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''


class Solution(object):
    def sumNumbers(self, root, r=0):
        if not root:
            return 0

        r = r * 10 + root.val
        return sum([
            self.sumNumbers(c, r) for c in (root.left, root.right)]) or r
