# -*- coding: utf-8 -*-

'''
Edit Distance
=============

Given two words word1 and word2, find the minimum number of steps required to
convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''


class Solution(object):
    '''算法思路：

    动态规划，假设 dp[i][j] 为从 word1[:i] 到 word2[:j] 的最小编辑距离，那么，
    word1[:i] = word1[:i - 1] + word1[i - 1]
    word2[:j] = word2[:j - 1] + word2[j - 1]

    - 如果 word1[:i - 1] + word1[i - 1] == word2[:j - 1], 那么只需删掉
      word2[j - 1] 就行了
    - 如果 word1[:i - 1] == word2[:j - 1] + word2[j - 1]，那么只需插入
      word1[i - 1] 就行了
    - 如果 word1[:i - 1] == word2[:j - 1]，如果 word1[i - 1] == word2[j - 1]，
      那么需要替换一下，或者不用替换

    综上，取 3 者最小值即可。
    '''
    def minDistance(self, word1, word2):
        m, n = map(len, (word1, word2))
        dp = [range(n + 1)] + [[i] + [0] * n for i in xrange(1, m + 1)]

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                dp[i][j] = min(
                    dp[i][j - 1] + 1,
                    dp[i - 1][j] + 1,
                    dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1])
                )

        return dp[m][n]


s = Solution()
print s.minDistance('a', 'ac')
