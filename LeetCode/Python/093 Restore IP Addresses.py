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

    每一部分要满足：part < 256 and 只能是 '0' 和 其他非以 '0' 开头的数字
    '''
    def dfs(self, s, parts):
        if not s and parts or not parts and s:
            return []

        if parts == 1:
            return [] if s[0] == '0' and len(s) > 1 or int(s) >= 256 else [[s]]

        r = []
        for i in range(len(s)):
            if i and s[0] == '0' or int(s[:i + 1]) >= 256:
                break

            r += [[s[:i + 1]] + p for p in self.dfs(s[i + 1:], parts - 1)]

        return r

    def restoreIpAddresses(self, s):
        return map('.'.join, self.dfs(s, 4))


s = Solution()
print s.restoreIpAddresses('010010')
