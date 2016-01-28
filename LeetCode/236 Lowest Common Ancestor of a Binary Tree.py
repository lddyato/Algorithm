# -*- coding: utf-8 -*-

'''
Lowest Common Ancestor of a Binary Tree
=======================================

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes v and w as the lowest node in T that has both v
and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another
example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of
itself according to the LCA definition.
'''


class Solution(object):
    '''算法思路：

    递归查找左右子树里边是否包含 p 和 q，如果左右子树分别包含，那说明当前节点即为
    LCA
    '''
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return

        if root in (p, q):
            return root

        left, right = [
            self.lowestCommonAncestor(c, p, q)
            for c in (root.left, root.right)]

        if left and right:
            return root

        return left or right
