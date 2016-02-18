# -*- coding: utf-8 -*-

'''
Best Time to Buy and Sell Stock with Cooldown
=============================================

Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell
the stock before you buy again).

After you sell your stock, you cannot buy stock on next day.
(ie, cooldown 1 day)

Example:

    prices = [1, 2, 3, 0, 2]
    maxProfit = 3
    transactions = [buy, sell, cooldown, buy, sell]
'''


class Solution(object):
    '''算法思路：

    画出状态机，根据状态机可以得到递推公式

    参考了：https://leetcode.com/discuss/72030/share-my-dp-solution-by-state-machine-thinking
    '''
    def maxProfit(self, prices):
        if not prices:
            return 0

        reset, sell, buy = 0, 0, -prices[0]
        for i in xrange(1, len(prices)):
            reset, buy, sell = (
                max(reset, sell), max(buy, reset - prices[i]), buy + prices[i])

        return max(sell, reset)


s = Solution()
print s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
