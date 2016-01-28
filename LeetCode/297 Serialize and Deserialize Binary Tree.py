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
    比如: 1:2:3:x:x:4:5:x:x:x:x
    '''
    def buildNode(self, val):
        return TreeNode(int(val)) if val != 'x' else None

    def serialize(self, root):
        queue = [root]
        [map(queue.append, (node.left, node.right)) for node in queue if node]
        return ':'.join(map(lambda n: n and str(n.val) or 'x', queue))

    def deserialize(self, data):
        queue, i, data = collections.deque(), 0, data.split(':')

        while i < len(data):
            if not queue:
                root = self.buildNode(data[i])
                queue.append(root)
                i += 1
                continue

            for _ in xrange(len(queue)):
                node = queue.popleft()
                node.left, node.right = [
                    self.buildNode(data[i + j]) for j in xrange(2)]

                [queue.append(c) for c in (node.left, node.right) if c]
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
