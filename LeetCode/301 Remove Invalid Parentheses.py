# -*- coding: utf-8 -*-

'''
Remove Invalid Parentheses
==========================

Remove the minimum number of invalid parentheses in order to make the input
string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''


class Solution(object):
    '''算法思路：

    首先计算出来总共有多少 pairs，然后 dfs 搜索出来 pairs 对即可。加入 l, r 是为了
    剪枝，提前把不符合要求的分支去掉
    '''
    def search(self, i, s, l, r, open, pairs, path, rs):
        if i == len(s) and not (open or pairs):
            rs.add(''.join(path))
            return

        if i == len(s) or min(l, r, open) < 0:
            return

        if s[i] == '(':
            self.search(i + 1, s, l - 1, r, open, pairs, path, rs)
            self.search(i + 1, s, l, r, open + 1, pairs, path + [s[i]], rs)
        elif s[i] == ')':
            self.search(i + 1, s, l, r - 1, open, pairs, path, rs)
            self.search(i + 1, s, l, r, open - 1, pairs - 1, path + [s[i]], rs)
        else:
            self.search(i + 1, s, l, r, open, pairs, path + [s[i]], rs)

    def removeInvalidParentheses(self, s):
        l, r, pairs = 0, 0, 0
        for char in s:
            if char == '(':
                l += 1
            elif char == ')' and l:
                l -= 1
                pairs += 1
            elif char == ')':
                r += 1

        rs = set()
        self.search(0, s, l, r, 0, pairs, [], rs)
        return list(rs)



s = Solution()
print s.removeInvalidParentheses("()())()")
