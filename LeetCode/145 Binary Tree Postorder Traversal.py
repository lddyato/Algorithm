# -*- coding: utf-8 -*-

'''
Binary Tree Postorder Traversal
===============================

Given a binary tree, return the postorder traversal of its tops' values.

For example:

Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
'''


class Solution(object):
    def postorderTraversal(self, root):
        return (sum(map(
            self.postorderTraversal, (root.left, root.right)), []) +
            [root.val]) if root else []


class Solution(object):
    '''算法思路：

    利用的原理是，后序遍历的结果 和 先访问node，然后再访问 node.right,
    最后访问 node.left 的结果是相反的
    '''
    def postorderTraversal(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                r.append(root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop().left

        return r[::-1]


class Solution(object):
    '''算法思路：

    用栈 + 标记，利用的原理同上
    '''
    def postorderTraversal(self, root):
        if not root:
            return []

        stack, r = [[root, 0]], []
        while stack:
            top = stack[-1]

            if top[1]:
                stack.pop()
                if top[0].left:
                    stack.append([top[0].left, 0])
            else:
                r.append(top[0].val)
                top[1] = 1

                if top[0].right:
                    stack.append([top[0].right, 0])

        return r[::-1]


class Solution(object):
    '''算法思路：

    Morris Traversal, based on Threaded Binary Tree
    '''
    def postorderTraversal(self, root):
        r = []
        while root:
            if not root.right:
                r.append(root.val)
                root = root.left
            else:
                next = root.right
                while next.left and next.left != root:
                    next = next.left

                if not next.left:
                    r.append(root.val)
                    next.left = root
                    root = root.right
                else:
                    root = root.left
        return r[::-1]
