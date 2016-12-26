# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        stack, sum, isLeft = [], 0, False

        while stack or root:
            if root:
                stack.append(root)

                if isLeft and not (root.left or root.right):
                    sum += root.val

                root, isLeft = root.left, True
            else:
                root, isLeft = stack.pop().right, False

        return sum


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
c.right = e

s = Solution()
print s.sumOfLeftLeaves(a)
