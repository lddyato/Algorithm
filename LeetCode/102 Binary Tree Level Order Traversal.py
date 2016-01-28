# -*- coding: utf-8 -*-

'''
Binary Tree Level Order Traversal
=================================

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''


class Solution(object):
    '''算法思路：

    BFS，队列里边包含当前 level 值
    '''
    def levelOrder(self, root):
        if not root:
            return []

        queue, result = [(root, 0)], []
        while queue:
            node, level = queue.pop(0)

            if level > len(result) - 1:
                result.append([node.val])
            else:
                result[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        return result


class Solution(object):
    '''算法思路：

    BFS，这种做法的依据是，随着上一层的遍历的完成，队列里边剩下的都是下一层的 node
    '''
    def levelOrder(self, root):
        if not root:
            return []

        queue, result = [root], []
        while queue:
            sublist, levelNum = [], len(queue)

            for i in xrange(levelNum):
                node = queue.pop(0)
                sublist.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(sublist)

        return result
