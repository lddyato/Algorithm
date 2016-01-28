# -*- coding: utf-8 -*-

'''
Best Time to Buy and Sell Stock III
===================================

Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete at most two
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must
sell the stock before you buy again).
'''


class Solution(object):
    '''算法思路：

    将 array 截成两段，每次算出左右最大profit的和，然后取和的最大值

    Time: O(n^2)

    结果：TLE
    '''
    def getMaxProfit(self, start, end):
        minPrice, maxPrice, profit = None, None, 0
        for i in xrange(start, end + 1):
            p = self.prices[i]
            if minPrice is None or p < minPrice:
                minPrice = maxPrice = p
            elif p > maxPrice:
                maxPrice = p
            profit = max(profit, maxPrice - minPrice)
        return profit

    def maxProfit(self, prices):
        profit, length, self.prices = 0, len(prices), prices
        for i in xrange(1, length):
            profit = max(
                profit,
                self.getMaxProfit(0, i) + self.getMaxProfit(i + 1, length - 1))
        return profit


class Solution(object):
    '''算法思路：

    预先将到开头和到结尾的最大profit分别算出来，然后同样将 array 分成两段，求两段和
    的最大值

    Time: O(n)

    结果：AC
    '''
    def getProfits(self, toEnd=False):
        r, minPrice, maxPrice, profit = [], None, None, 0
        for p in (self.prices[::-1] if toEnd else self.prices):
            bigger, smaller = p > maxPrice, p < minPrice

            if minPrice is None or [smaller, bigger][toEnd]:
                minPrice = maxPrice = p
            elif [bigger, smaller][toEnd]:
                if toEnd:
                    minPrice = p
                else:
                    maxPrice = p
            profit = max(profit, maxPrice - minPrice)

            r.append(profit)
        return (r[::-1] + [0]) if toEnd else r

    def maxProfit(self, prices):
        self.prices = prices

        (toStart, toEnd), profit = map(self.getProfits, (False, True)), 0
        for i in xrange(len(prices)):
            profit = max(profit, toStart[i] + toEnd[i + 1])

        return profit


s = Solution()
print s.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0])
