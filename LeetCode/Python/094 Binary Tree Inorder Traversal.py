# -*- coding: utf-8 -*-

'''
Binary Tree Inorder Traversal
=============================

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''


class Solution(object):
    '''算法思路:

    递归
    '''
    def inorderTraversal(self, root):
        if not root:
            return []

        left, right = map(self.inorderTraversal, (root.left, root.right))
        return left + [root.val] + right


class Solution(object):
    '''算法思路：

    用栈
    '''
    def inorderTraversal(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                r.append(root.val)
                root = root.right
        return r


class Solution(object):
    '''算法思路：

    Morris Traversal, based on Threaded Binary Tree
    '''
    def inorderTraversal(self, root):
        r = []
        while root:
            if not root.left:
                r.append(root.val)
                root = root.right
            else:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right

                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    r.append(root.val)
                    root = root.right
        return r
