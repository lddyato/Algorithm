# -*- coding: utf-8 -*-

'''
Palindrome Partitioning II
==========================

Given a string s, partition s such that every substring of the partition is a
palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using
1 cut.
'''


class Solution(object):
    '''算法思路：

    DP, dp[i] 表示以第 i 位结束的字串最小 cut 次数

    dp[i] = min(i 前面的每一个回文子串前面的子串 + 1)

    结果：TLE
    '''
    def isPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def minCut(self, s):
        dp, n = [-1] * (len(s) + 1), len(s)

        for i in xrange(1, n + 1):
            dp[i] = min(
                dp[j - 1] + 1
                for j in xrange(i, 0, -1)
                if self.isPalindrome(s, j - 1, i - 1)
            )
        return dp[n]


class Solution(object):
    '''算法思路：

    同上，每次判断字串是否是回文字串花费了大量时间，先把结果缓存起来

    结果：AC
    '''
    def minCut(self, s):
        n = len(s)
        dp, record = [-1] * (n + 1), [[True] * n for _ in xrange(n)]

        # 计算每个子串是不是回文串是有技巧的，以步长从小到大的顺序，判断除去两端后剩下
        # 的子串是否是回文即可
        # for steps in xrange(n):
        #     for i in xrange(0, n - steps):
        #         record[i][i + steps] = (
        #             steps < 2 or record[i + 1][i + steps - 1]) and (
        #             s[i] == s[i + steps])

        for i in xrange(n):
            r1 = r2 = 0
            while i - r1 >= 0 and i + r1 < n:
                record[i - r1][i + r1] = (
                    (r1 == 0 or record[i - r1 + 1][i + r1 - 1]) and
                    s[i - r1] == s[i + r1])
                r1 += 1

            while i - r2 >= 0 and i + 1 + r2 < n:
                record[i - r2][i + 1 + r2] = (
                    (r2 == 0 or record[i - r2 + 1][i + r2]) and
                    s[i - r2] == s[i + 1 + r2])
                r2 += 1

        for i in xrange(1, n + 1):
            dp[i] = min(
                dp[j - 1] + 1 for j in xrange(i, 0, -1) if record[j - 1][i - 1]
            )

        return dp[n]


class Solution(object):
    '''算法思路：

    以每一个元素为中心，不断扩大半径搜索，dp[i] 表示从 0 到 i-1 的字串最小 cut 次数，
    递推方程和上面一样

    结果：AC
    '''
    def minCut(self, s):
        n = len(s)
        dp = [i for i in xrange(-1, n)]

        for i in xrange(n):
            r1 = r2 = 0
            # 奇数长度
            while i - r1 >= 0 and i + r1 < n and s[i - r1] == s[i + r1]:
                dp[i + r1 + 1] = min(dp[i + r1 + 1], dp[i - r1] + 1)
                r1 += 1

            # 偶数长度
            while i - r2 >= 0 and i + 1 + r2 < n and s[i - r2] == s[i + 1 + r2]:
                dp[i + 2 + r2] = min(dp[i + 2 + r2], dp[i - r2] + 1)
                r2 += 1

        return dp[-1]


s = Solution()
print s.minCut("aaa")
