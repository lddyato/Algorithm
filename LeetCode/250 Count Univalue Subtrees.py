# -*- coding: utf-8 -*-

'''
Count Univalue Subtrees
=======================

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,

              5
             / \
            1   5
           / \   \
          5   5   5

return 4.
'''


class Solution(object):
    '''算法思路：

    分治

    isSame() 返回该 subtree 是否每个节点都相等，如果左右子树和 root value 相等，则+1
    '''
    def isSame(self, root):
        if not root:
            return True

        left, right = map(self.isSame, (root.left, root.right))
        if left and right and (
                root.left.val == root.val if root.left else True) and (
                root.right.val == root.val if root.right else True):
            self.sum += 1
            return True
        return False

    def countUnivalSubtrees(self, root):
        self.sum = 0
        self.isSame(root)
        return self.sum


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return '<TreeNode {}>'.format(self.val)


a = TreeNode(5)
b = TreeNode(1)
c = TreeNode(3)
d = TreeNode(1)
e = TreeNode(1)
f = TreeNode(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

s = Solution()
print s.countUnivalSubtrees(a)
