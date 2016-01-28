# -*- coding: utf-8 -*-

'''
Construct Binary Tree from Inorder and Postorder Traversal
==========================================================

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''


class Solution(object):
    '''算法思路：

    可以将 postorder 翻转一下变成 先遍历节点，再遍历右子树，最后遍历左子树，和中序对应
    即可

    结果：Memory Limit Exceeded
    '''
    def build(self, inorder, preorder):
        if not inorder:
            return

        root, i = TreeNode(preorder[0]), inorder.index(preorder[0])

        root.right = self.build(inorder[i+1:], preorder[1:len(inorder) - i])
        root.left = self.build(inorder[:i], preorder[len(inorder) - i:])

        return root

    def buildTree(self, inorder, postorder):
        return self.build(inorder, postorder[::-1])


class Solution(object):
    '''算法思路：

    同上，不过不再每次生成新的数组，而是用 pointer 代替

    结果：AC
    '''
    def build(self, inorder, inStart, inEnd, preorder, preStart):
        if inStart > inEnd:
            return

        root, i = TreeNode(preorder[preStart]), self.r[preorder[preStart]]

        root.right = self.build(inorder, i + 1, inEnd, preorder, preStart + 1)
        root.left = self.build(
            inorder, inStart, i - 1, preorder, preStart + inEnd - i + 1)

        return root

    def buildTree(self, inorder, postorder):
        self.r = {v: i for i, v in enumerate(inorder)}
        return self.build(inorder, 0, len(inorder) - 1, postorder[::-1], 0)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


s = Solution()
root = s.buildTree([2,1,3], [2,3,1])

queue = [root]
for node in queue:
    if node:
        print node
        queue += [node.left, node.right]
