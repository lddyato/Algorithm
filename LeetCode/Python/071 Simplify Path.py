# -*- coding: utf-8 -*-

'''
Simplify Path
=============

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''


class Solution(object):
    '''算法思路：

    首先将 path 以 '/' 分开，对每一部分分开处理，需要注意的是，path中带有 `.` 的部分
    '''
    def simplifyPath(self, path):
        stack = []

        for p in path.split('/'):
            if p == '..' and stack:
                stack.pop()
            elif p and p not in ['.', '..']:
                stack.append(p)

        return '/{}'.format('/'.join(stack))


s = Solution()
print s.simplifyPath('/../home/')
print s.simplifyPath('/home/..')
