# -*- coding: utf-8 -*-

'''
Paint House
===========

There are a row of n houses, each house can be painted with one of the three
colors: red, blue or green. The cost of painting each house with a certain
color is different. You have to paint all the houses such that no two adjacent
houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3
cost matrix. For example, costs[0][0] is the cost of painting house 0 with
color red; costs[1][2] is the cost of painting house 1 with color green, and
so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.
'''


class Solution(object):
    '''算法思路：

    DP

    设 color 总共有 color0, color1, color2 三种，f(n, color1) 为第 n 个 house 涂
    上 color0 后总的最小的 costs，则递推公式为：

    f(n, color0) = min(f(n-1, color1), f(n-1, color2)) + costs[n][color0]

    Time: O(n)
    Space: O(n)
    '''
    def minCost(self, costs):
        if not costs:
            return 0

        dp = [[0] * 3 for i in xrange(len(costs))]

        [dp[i].__setitem__(j, costs[i][j] +
         (min(dp[i - 1][:j] + dp[i - 1][j + 1:]) if i > 0 else 0))
         for i in xrange(len(costs))
         for j in xrange(3)]

        return min(dp[-1])


class Solution(object):
    '''算法思路：

    同上，不过只用了 const 空间

    Time: O(n)
    Space: O(1)
    '''
    def minCost(self, costs):
        house = [0] * 3
        for cost in costs:
            house = [min(house[:j] + house[j+1:]) + cost[j] for j in xrange(3)]
        return min(house)


s = Solution()
print s.minCost([
    [1, 2, 4],
    [3, 0, 1],
    [2, 3, 4]
])
