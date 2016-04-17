# -*- coding: utf-8 -*-

'''
Serialize and Deserialize Binary Tree
=====================================

Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a
binary tree. You do not necessarily need to follow this format, so please be
creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your
serialize and deserialize algorithms should be stateless.
'''


import collections


class Codec(object):
    '''算法思路：

    利用 BFS 生成类似 leetcode 上面用的二叉树表示的格式
    比如: 1:2:3:#:#:#:5:#:#:#:#
    '''
    def buildNode(self, val):
        return None if val == '#' else TreeNode(int(val))

    def serialize(self, root):
        queue = [root]
        for node in queue:
            if not node:
                continue
            queue += [node.left, node.right]

        return ':'.join(
            map(lambda item: str(item.val) if item else '#', queue))

    def deserialize(self, data):
        parts = data.split(':')
        root = self.buildNode(parts[0])
        queue, i = collections.deque([root]), 1

        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = map(
                    self.buildNode, (parts[i], parts[i + 1]))
                queue.append(node.left)
                queue.append(node.right)
                i += 2
        return root


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c
c.left = d
c.right = e

codec = Codec()
s = codec.serialize(a)
print s
root = codec.deserialize(s)
print codec.serialize(root)
