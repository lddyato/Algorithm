# -*- coding: utf-8 -*-

'''
Restore IP Addresses
====================

Given a string containing only digits, restore it by returning all possible
valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''


class Solution(object):
    '''算法思路：

    递归

    每一部分要满足：

    len(part) == 1
    or
    len(part) > 1 and int(part) <= 255 and not part.startswith('0')

    如果 len(part) > 1，part 不能以 '0' 开头，这一点容易忽略
    '''
    def parse(self, s, part):
        if part == 4 and (
                len(s) == 1 or
                len(s) > 1 and int(s) <= 255 and not s.startswith('0')):
            return [[s]]

        reuslt, i, prefix = [], 0, ''
        while i < min(3, len(s)):
            prefix += s[i]

            if int(prefix) <= 255 and not (
                    len(prefix) > 1 and
                    prefix.startswith('0')) and part + 1 <= 4:

                left = self.parse(s[i+1:], part + 1)
                if left and len(left[0]) == 4 - part:
                    reuslt += [[prefix] + p for p in left]
            i += 1

        return reuslt

    def restoreIpAddresses(self, s):
        return map(lambda p: '.'.join(p), self.parse(s, 1))


s = Solution()
print s.restoreIpAddresses('010010')
