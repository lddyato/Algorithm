# -*- coding: utf-8 -*-

'''
Binary Tree Right Side View
===========================

Given a binary tree, imagine yourself standing on the right side of it, return
the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

You should return [1, 3, 4].
'''


class Solution(object):
    '''算法思路：

    BFS，不过换成先遍历右子树，再遍历左子树，然后把每一层的第一个元素返回回来
    '''
    def rightSideView(self, root):
        if not root:
            return []

        r = [[root]]
        while r[-1]:
            r.append([
                c for node in r[-1] for c in (node.left, node.right) if c])

        return map(lambda item: item[-1].val, r[:-1])
