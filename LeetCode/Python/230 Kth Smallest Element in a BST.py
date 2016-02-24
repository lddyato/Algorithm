# -*- coding: utf-8 -*-

'''
Kth Smallest Element in a BST
=============================

Given a binary search tree, write a function kthSmallest to find the kth
smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to
find the kth smallest frequently? How would you optimize the kthSmallest
routine?
'''


class Solution(object):
    '''算法思路：

    中序遍历

    Time: O(n)
    '''
    def kthSmallest(self, root, k):
        stack, queue = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                queue.append(root.val)
                if len(queue) == k:
                    return queue[-1]
                root = root.right


class Solution(object):
    '''算法思路：

    利用 BST 的特性

    Time: O(n)
    '''
    def countNode(self, root):
        return root and sum(
            map(self.countNode, (root.left, root.right)), 1) or 0

    def kthSmallest(self, root, k):
        count = self.countNode(root.left)
        if count == k - 1:
            return root.val

        return self.kthSmallest(
            root.left, k) if count > k - 1 else self.kthSmallest(
            root.right, k - count - 1)
