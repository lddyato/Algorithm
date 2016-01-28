# -*- coding: utf-8 -*-

'''
Closest Binary Search Tree Value II
===================================

Given a non-empty binary search tree and a target value, find k values in the
BST that are closest to the target.

Note:

- Given target value is a floating point.
- You may assume k is always valid, that is: k ≤ total nodes.
- You are guaranteed to have only one unique set of k values in the BST that
  are closest to the target.

Follow up:

Assume that the BST is balanced, could you solve it in less than O(n) runtime
(where n = total nodes)?
'''


import bisect


class Solution(object):
    '''算法思路：

    首先中序遍历整个树，得到序列后二分查找 target 的位置 i，从 i 处将序列分成两部分,
    然后将前半部分反转，归并排序得到前 k 个离 target 最近的序列，此序列从前往后依次离
    target 越来越远
    '''
    def closestKValues(self, root, target, k):
        stack, r = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                r.append(root.val)
                root = root.right

        i = bisect.bisect(r, target)
        l1, l2, = r[i:], r[:i][::-1]

        i, j, r = 0, 0, []
        while i < len(l1) and j < len(l2) and len(r) < k:
            if abs(l1[i] - target) < abs(l2[j] - target):
                r.append(l1[i])
                i += 1
            else:
                r.append(l2[j])
                j += 1

        r += (l1[i:] or l2[j:])[:k - len(r)]
        return r


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(5)
a = TreeNode(2)
b = TreeNode(7)
c = TreeNode(0)
d = TreeNode(4)
e = TreeNode(6)
f = TreeNode(9)

root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f

s = Solution()
print s.closestKValues(root, 5.7, 5)
