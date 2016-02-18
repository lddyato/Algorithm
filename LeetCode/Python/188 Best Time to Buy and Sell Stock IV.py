# -*- coding: utf-8 -*-

'''
Best Time to Buy and Sell Stock IV
==================================

Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete at most k
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell
the stock before you buy again).
'''


class Solution(object):
    '''算法思路：

    动态规划

    dp[i][j] 表示截止到第 j 天一共交易了 i 次，最大盈利。那么
    dp[i][j] = max(dp[i][0..n-1])，即在能够取得最大利益的一天交易第 i 次

    我们用 transaction 来表示第 i 天交易所能获得的最大的利益，那么

    transaction[i] = max(
        dp[i - 1][j - 1] + max(profit, 0),  # 昨天交易了第 i - 1 次，今天交易第 i 次
        transaction + profit)               # 取消前一天的卖出，改为第 j 天卖出
    '''
    def maxProfit(self, k, prices):
        n = len(prices)

        if k >= n >> 1:
            return sum([
                max(prices[i] - prices[i - 1], 0) for i in xrange(1, n)])

        dp = [[0] * n for _ in xrange(k + 1)]
        for i in xrange(1, k + 1):
            transaction = 0
            for j in xrange(1, n):
                profit = prices[j] - prices[j - 1]
                transaction = max(
                    dp[i - 1][j - 1] + max(profit, 0),
                    transaction + profit)
                dp[i][j] = max(dp[i][j - 1], transaction)
        return dp[k][-1]
