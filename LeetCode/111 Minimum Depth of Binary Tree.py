# -*- coding: utf-8 -*-

'''
Minimum Depth of Binary Tree
============================

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the
root node down to the nearest leaf node.
'''


class Solution(object):
    '''算法思路：

    先序遍历，DFS

    相对于找 Maximum Depth，这里不能根据当前节点是否为 None 进行判断
    原因在于：当根据当前节点是否为 None 进行判断时，Maximum 最终结果一定在于叶节点上，
    而 Minimum 有可能为单孩子节点
    '''
    def search(self, root, depth=0):
        depth += 1

        if not root.left and not root.right:
            self.min = depth if self.min is None else min(self.min, depth)
            return

        if root.left:
            self.search(root.left, depth)

        if root.right:
            self.search(root.right, depth)

    def minDepth(self, root):
        if not root:
            return 0

        self.min = None
        self.search(root)
        return self.min


class Solution(object):
    '''算法思路：

    BFS，层序遍历
    '''
    def minDepth(self, root):
        if not root:
            return 0

        queue, level = [root], 1
        while queue:
            for i in xrange(len(queue)):
                node = queue.pop(0)

                if not node.left and not node.right:
                    return level

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1
