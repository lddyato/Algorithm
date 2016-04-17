# -*- coding: utf-8 -*-

'''
The thief has found himself a new place for his thievery again. There is only
one entrance to this area, called the "root." Besides the root, each house has
one and only one parent house. After a tour, the smart thief realized that "all
houses in this place forms a binary tree". It will automatically contact the
police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without
alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
'''


def cache(f):
    def method(obj, root, robbed):
        key = '{}:{}'.format(id(root), robbed)
        if key not in obj.cache:
            obj.cache[key] = f(obj, root, robbed)
        return obj.cache[key]
    return method


class Solution(object):
    '''算法思路：

    记忆化搜索
    '''
    def __init__(self):
        self.cache = {}

    @cache
    def dfs(self, root, robbed):
        if not root:
            return 0

        if robbed:
            return self.dfs(root.left, False) + self.dfs(root.right, False)

        return max(
            self.dfs(root.left, False) + self.dfs(root.right, False),
            self.dfs(root.left, True) + self.dfs(root.right, True) + root.val
        )

    def rob(self, root):
        return self.dfs(root, False)
