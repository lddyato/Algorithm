# -*- coding: utf-8 -*-

'''
Populating Next Right Pointers in Each Node II
==============================================

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution
still work?

Note:

- You may only use constant extra space.

For example,
Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''


class Solution(object):
    '''算法思路：

    同 166 第一种解法，但依旧用了 queue
    '''
    def connect(self, root):
        if not root:
            return

        queue = [root]
        while queue:
            pre = None
            for i in xrange(len(queue)):
                peek = queue.pop(0)
                peek.next, pre = pre, peek

                [queue.append(c) for c in (peek.right, peek.left) if c]


class Solution(object):
    '''算法思路：

    先访问 当前节点，再访问 右孩子，最后访问 左孩子，依次连接
    '''
    def connect(self, root):
        if not (root and (root.left or root.right)):
            return

        if root.left and root.right:
            root.left.next = root.right

        next = root.next
        while next and not (next.left or next.right):
            next = next.next

        if next:
            (root.right or root.left).next = next.left or next.right

        map(self.connect, (root.right, root.left))
