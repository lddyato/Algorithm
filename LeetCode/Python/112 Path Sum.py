# -*- coding: utf-8 -*-

'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

For example:

Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


class Solution(object):
    '''算法思路：

    递归求解
    '''
    def hasPathSum(self, root, sum):
        if not root:
            return False

        sum -= root.val

        if not (root.left or root.right or sum):
            return True

        return self.hasPathSum(
            root.left, sum) or self.hasPathSum(root.right, sum)
