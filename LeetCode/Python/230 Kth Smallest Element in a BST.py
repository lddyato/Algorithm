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
    def search(self, root):
        if self.r is not None or not root:
            return

        self.search(root.left)

        self.k -= 1
        if not self.k:
            self.r = root.val

        self.search(root.right)

    def kthSmallest(self, root, k):
        self.k = k
        self.r = None

        self.search(root)
        return self.r


class Solution(object):
    '''算法思路：

    利用二分
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
