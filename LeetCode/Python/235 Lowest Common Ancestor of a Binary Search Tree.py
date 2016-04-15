# -*- coding: utf-8 -*-

'''
Lowest Common Ancestor of a Binary Search Tree
==============================================

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes v and w as the lowest node in T that has both v and
w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another
example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of
itself according to the LCA definition.
'''


class Solution(object):
    '''算法思路：

    由于是二分查找树，因此找到第一个使得 p，q 分别在左右子树上的节点
    '''
    def lowestCommonAncestor(self, root, p, q):
        if (root.val - p.val) * (root.val - q.val) <= 0:
            return root

        return self.lowestCommonAncestor(
            root.left if p.val < root.val else root.right, p, q)
