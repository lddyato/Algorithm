# -*- coding: utf-8 -*-

'''
Recover Binary Search Tree
==========================

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a
constant space solution?
'''


class Solution(object):
    '''算法思路：

    中序遍历，然后从序列里边找到两个被 swapped 的点，这里题意其实有点模糊，应该明确的
    说明是 swap 了值

    Space：O(n)
    '''
    def recoverTree(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                r.append(root)
                root = root.right

        one, two = None, None
        for i in xrange(1, len(r)):
            if r[i].val < r[i - 1].val:
                one, two = one or r[i - 1], r[i]
        one.val, two.val = two.val, one.val
