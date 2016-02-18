# -*- coding: utf-8 -*-

'''
Count Complete Tree Nodes
=========================

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees

In a complete binary tree every level, except possibly the last, is completely
filled, and all nodes in the last level are as far left as possible. It can
have between 1 and 2h nodes inclusive at the last level h.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    '''算法思路：

    完全遍历

    Time: O(n)

    结果：TLE
    '''
    def countNodes(self, root):
        if not root:
            return 0

        queue = [root]
        for node in queue:
            [queue.append(c) for c in (node.left, node.right) if c]

        return len(queue)


class Solution(object):
    '''算法思路：

    除去最后一层的个数 + 最后一层的个数

    结果：勉强 AC
    '''
    def getHeight(self, root):
        height = 0
        while root:
            root = root.left
            height += 1
        return height

    def countNodes(self, root):
        if not root:
            return 0

        height = self.getHeight(root)

        stack, depth, count = [], 0, 0
        while stack or root:
            if root:
                depth += 1

                stack.append([root, depth])
                root = root.left

                if not root:
                    if depth != height:
                        break
                    count += 1
            else:
                root, depth = stack.pop()
                root = root.right


        return (1 << height - 1) - 1 + count


class Solution(object):
    '''算法思路：

    分别计算左右子树的高度，如果左右子树高度一致，那么最后一个叶节点一定在右子树上，
    如果左右子树高度不一样，那么最后一个叶节点一定在左子树上
    '''
    def getHeight(self, root):
        height = 0
        while root:
            root = root.left
            height += 1
        return height

    def countNodes(self, root):
        if not root:
            return 0

        l, r = map(self.getHeight, (root.left, root.right))
        shift, child = (l, root.right) if l == r else (r, root.left)
        return (1 << shift) + self.countNodes(child)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


a = TreeNode(0)
b = TreeNode(1)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

s = Solution()
print s.countNodes(a)
