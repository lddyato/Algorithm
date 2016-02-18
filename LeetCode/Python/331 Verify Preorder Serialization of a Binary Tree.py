# -*- coding: utf-8 -*-

'''
Verify Preorder Serialization of a Binary Tree
==============================================

One way to serialize a binary tree is to use pre-order traversal. When we
encounter a non-null node, we record the node's value. If it is a null node,
we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

For example, the above binary tree can be serialized to the string
"9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct
preorder traversal serialization of a binary tree. Find an algorithm without
reconstructing the tree.

Each comma separated value in the string must be either an integer or a
character '#' representing null pointer.

You may assume that the input format is always valid, for example it could
never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
'''


class Solution(object):
    '''算法思路：

    不能重建二叉树，联想到我们遍历二叉树的时候会使用 stack，所以考虑用栈，首先排除边界
    条件：开头为 '#' 的和结尾不为 '#'的，然后遍历 preorder 每逢碰到 '#'，从栈 pop，
    最后判断 stack 是否为空即可
    '''
    def isValidSerialization(self, preorder):
        preorder = preorder.split(',')

        if preorder[0] == '#' and len(preorder) > 1 or preorder[-1] != '#':
            return False

        preorder = preorder[:-1]
        stack = preorder[:1]

        for i in xrange(1, len(preorder)):
            if preorder[i] == '#':
                if not stack:
                    return False
                stack.pop()
            else:
                stack.append(preorder[i])

        return not stack


s = Solution()
print s.isValidSerialization('#')
