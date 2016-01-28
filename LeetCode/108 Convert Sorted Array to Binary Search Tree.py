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
    def sortedArrayToBST(self, nums, start=0, end=None):
        end = (len(nums) - 1) if end is None else end

        if start > end:
            return
        if start == end:
            return TreeNode(nums[start])

        mid = (start + end) / 2

        root = TreeNode(nums[mid])
        root.left, root.right = (
            self.sortedArrayToBST(nums, start, mid - 1),
            self.sortedArrayToBST(nums, mid + 1, end))

        return root
