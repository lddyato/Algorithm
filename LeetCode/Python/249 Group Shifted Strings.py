# -*- coding: utf-8 -*-

'''
Group Shifted Strings
=====================

Given a string, we can "shift" each of its letter to its successive letter,
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all
strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the
lexicographic order.
'''


class Solution(object):
    '''算法思路：

    找到共同点，利用 hash 把具有共同点的 word 并到一起
    '''
    def groupStrings(self, strings):
        r, record = [], {}

        for s in strings:
            key = '%s:' % len(s)
            for char in s:
                key += str((ord(char) - ord(s[0]) + 26) % 26)

            record.setdefault(key, []).append(s)

        return map(sorted, record.values())


s = Solution()
print s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
