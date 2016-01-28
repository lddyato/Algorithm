# -*- coding: utf-8 -*-

'''
Interleaving String
===================

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''


def cache(f):
    def method(*args):
        obj = args[0]
        key = '{}:{}:{}'.format(*args[1:])

        record = getattr(obj, 'record', {})
        if not record:
            setattr(obj, 'record', record)

        if key not in record:
            record[key] = f(*args)
        return record[key]
    return method


class Solution(object):
    '''算法思路：

    DFS + cache
    '''
    @cache
    def search(self, i1, i2, i3):
        if i1 >= len(self.s1) or i2 >= len(self.s2):
            i, s = (i2, self.s2) if i1 >= len(self.s1) else (i1, self.s1)

            while i < len(s):
                if s[i] != self.s3[i3]:
                    return False
                i += 1
                i3 += 1
            return True

        if self.s1[i1] == self.s2[i2] == self.s3[i3]:
            if not self.search(i1 + 1, i2, i3 + 1):
                return self.search(i1, i2 + 1, i3 + 1)
            return True

        if self.s1[i1] == self.s3[i3]:
            return self.search(i1 + 1, i2, i3 + 1)

        if self.s2[i2] == self.s3[i3]:
            return self.search(i1, i2 + 1, i3 + 1)

        return False

    def isInterleave(self, s1, s2, s3):
        len1, len2, len3 = map(len, (s1, s2, s3))
        if len3 != len1 + len2:
            return False

        self.s1, self.s2, self.s3 = s1, s2, s3

        return self.search(0, 0, 0)


s = Solution()
print s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
