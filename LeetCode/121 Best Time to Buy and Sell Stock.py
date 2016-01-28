# -*- coding: utf-8 -*-

'''
Best Time to Buy and Sell Stock
===============================

Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.
'''


class Solution(object):
    '''算法思路：

    以最小的价格买入，以最大的价格卖出。
    '''
    def maxProfit(self, prices):
        minPrice, maxPrice, profit = None, None, 0
        for p in prices:
            if minPrice is None or p < minPrice:
                minPrice = maxPrice = p
            elif p > maxPrice:
                maxPrice = p
            profit = max(profit, maxPrice - minPrice)
        return profit
