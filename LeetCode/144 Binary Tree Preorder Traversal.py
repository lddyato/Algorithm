# -*- coding: utf-8 -*-

'''
Binary Tree Preorder Traversal
==============================

Given a binary tree, return the preorder traversal of its nodes' values.

For example:

Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
'''


class Solution(object):
    '''算法思路：

    递归
    '''
    def preorderTraversal(self, root):
        return (([root.val] + sum(
                map(self.preorderTraversal, (root.left, root.right)), []))
                if root else [])


class Solution(object):
    '''算法思路：

    用栈，先压 right，再压 left
    '''
    def preorderTraversal(self, root):
        if not root:
            return []

        stack, r = [root], []
        while stack:
            node = stack.pop()
            stack.append(node.val)
            [stack.append(child) for child in (node.right, node.left) if child]

        return r


class Solution(object):
    '''算法思路：

    另外一种用栈的写法
    '''
    def preorderTraversal(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                stack.append(root)
                r.append(root.val)
                root = root.left
            else:
                root = stack.pop().right
        return r


class Solution(object):
    '''算法思路：

    用栈 + 标记法
    '''
    def preorderTraversal(self, root):
        if not root:
            return []

        stack, r = [[root, 0]], []
        while stack:
            top = stack[-1]

            if top[1]:
                stack.pop()
                if top[0].right:
                    stack.append([top[0].right, 0])
            else:
                r.append(top[0].val)
                top[1] = 1

                if top[0].left:
                    stack.append([top[0].left, 0])
        return r


class Solution(object):
    '''算法思路：

    Morris Traversal, based on Threaded Binary Tree
    '''
    def preorderTraversal(self, root):
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
                    r.append(root.val)
                    pre.right = root
                    root = root.left
                else:
                    root = root.right
        return r
