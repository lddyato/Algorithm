# -*- coding: utf-8 -*-

'''
Coin Change
===========

You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need to
make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''


class Solution(object):
    '''算法思路：

    动态规划，递归公式为：f(n) = min(f(n - c1), f(n - c2), ...) + 1

    Time: O(m*n)
    Space: O(m)

    note：m 为 amount, n 为 coins 数组长度
    '''
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in xrange(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]


s = Solution()
print s.coinChange([19,28,176,112,30,260,491,128,70,137,253], 8539)
