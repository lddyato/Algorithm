# -*- coding: utf-8 -*-

'''
Populating Next Right Pointers in Each Node
===========================================

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

- You may only use constant extra space.
- You may assume that it is a perfect binary tree (ie, all leaves are at the
  same level, and every parent has two children).

For example,
Given the following perfect binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''


class Solution(object):
    '''算法思路：

    层序遍历，不过是从右往左遍历，由于用了队列，因此虽然AC了，但是不符合题意
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

    先访问该节点，然后访问右节点，最后访问左子树
    '''
    def connect(self, root):
        if not (root and root.left):
            return

        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left

        self.connect(root.right)
        self.connect(root.left)
