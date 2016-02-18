# -*- coding: utf-8 -*-

'''
Symmetric Tree
==============

Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    '''算法思路：

    先序遍历: 一个先 visit right child，另一个先 visit left child，把结果保存起来
    然后比较

    此题用中序遍历比较麻烦
    '''
    def search(self, root, array, leftFirst):
        array.append(root.val if root else root)

        if root:
            [self.search(child, array, leftFirst) for child in ((
             root.left, root.right) if leftFirst else (root.right, root.left))]

    def isSymmetric(self, root):
        l1, l2 = [], []
        [self.search(root, *args) for args in ((l1, True), (l2, False))]
        return l1 == l2


class Solution(object):
    '''算法思路：

    遍历的过程中直接比较
    '''
    def search(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.search(p.left, q.right) and self.search(p.right, q.left)

    def isSymmetric(self, root):
        return self.search(root.left, root.right) if root else True


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(3)

a.left = b
a.right = c
b.left = d
c.right = e

s = Solution()
print s.isSymmetric(a)
