# -*- coding: utf-8 -*-

'''
Verify Preorder Sequence in Binary Search Tree
==============================================

Given an array of numbers, verify whether it is the correct preorder traversal
sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?
'''


class Solution(object):
    '''算法思路：

    每次找到子树的最大值，append 树顶，如果当前 num < 左子树的最大值，那就说明不是
    preorder
    '''
    def verifyPreorder(self, preorder):
        stack, root = [], float('-inf')
        for num in preorder:
            if num < root:
                return False

            while stack and num > stack[-1]:
                root = stack.pop()
            stack.append(num)
        return True


class Solution(object):
    '''算法思路：

    同上，不过 reuse preorder
    '''
    def verifyPreorder(self, preorder):
        i, root = 0, float('-inf')
        for num in preorder:
            if num < root:
                return False

            while i > 0 and num > preorder[i - 1]:
                root = preorder[i - 1]
                i -= 1

            preorder[i] = num
            i += 1

        return True


s = Solution()
print s.verifyPreorder([1, 3, 4, 2])
