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
    def compareVersion(self, version1, version2):
        vs1, vs2 = version1.split('.'), version2.split('.')
        len1, len2 = len(vs1), len(vs2)

        i = 0
        while i < min(len1, len2):
            if int(vs1[i]) < int(vs2[i]):
                return -1

            if int(vs1[i]) > int(vs2[i]):
                return 1

            i += 1

        if len1 == len2:
            return 0

        more, less = vs1, vs2
        if len1 < len2:
            more, less = vs2, vs1

        i = len(less)
        while i < len(more):
            if int(more[i]) != 0:
                return [-1, 1][more == vs1]

            i += 1

        return 0


s = Solution()
print s.compareVersion('1.0', '1.0.0')
