# -*- coding: utf-8 -*-

'''
Compare Version Numbers
=======================

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise
return 0.

You may assume that the version strings are non-empty and contain only digits
and the . character.

The . character does not represent a decimal point and is used to separate
number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is
the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''


class Solution(object):
    '''算法思路：

    占位比较，利用了占位思想
    '''
    def compareVersion(self, version1, version2):
        version1, version2 = version1.split('.'), version2.split('.')
        len1, len2 = map(len, (version1, version2))

        i = 0
        while i < max(len1, len2):
            a = int(version1[i]) if i < len1 else 0
            b = int(version2[i]) if i < len2 else 0

            r = cmp(a, b)
            if r:
                return r
            i += 1

        return 0


s = Solution()
print s.compareVersion('1.0', '1.0.0')
