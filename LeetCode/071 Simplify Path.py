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
    def simplifyPath(self, path):
        record = []

        i, length = 0, len(path)
        while i < length:
            part = ''
            while i < length and path[i] != '/':
                part += path[i]
                i += 1

            if part == '..' and record:
                del record[-1]

            if part not in ['', '.', '..']:
                record.append(part)

            i += 1

        return '/' + '/'.join(record)


s = Solution()
print s.simplifyPath('/../home/')
print s.simplifyPath('/home/..')
