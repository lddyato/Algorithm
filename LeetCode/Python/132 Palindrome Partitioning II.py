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

    动态规划，每次判断字串是否是回文字串花费了大量时间，先把结果缓存起来

    dp[i]: 总共分为了几段

    结果：AC
    '''
    def minCut(self, s):
        n = len(s)
        isPalindrome = [[False] * n for _ in range(n)]

        for r in range(1, n + 1):
            for i in range(n - r + 1):
                if r == 1:
                    isPalindrome[i][i + r - 1] = True
                    continue

                isPalindrome[i][i + r - 1] = (
                    isPalindrome[i + 1][i + r - 2] if r >= 3 else True
                ) and s[i] == s[i + r - 1]

        dp = range(n + 1)
        for i in range(2, n + 1):
            for j in range(i, 0, -1):
                if isPalindrome[j - 1][i - 1]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
        return dp[-1] - 1



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
