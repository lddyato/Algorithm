# -*- coding: utf-8 -*-

'''
Convert Sorted Array to Binary Search Tree
==========================================

Given an array where elements are sorted in ascending order, convert it to a
height balanced BST.
'''


class Solution(object):
    '''算法思路：

    中间的为 root
    '''
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) >> 1
        root = TreeNode(nums[mid])
        root.left, root.right = self.sortedArrayToBST(
            nums[:mid]), self.sortedArrayToBST(nums[mid + 1:])
        return root
