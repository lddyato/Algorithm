# -*- coding: utf-8 -*-

'''
Paint House II
==============

There are a row of n houses, each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different. You have to
paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k
cost matrix. For example, costs[0][0] is the cost of painting house 0 with
color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...

Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?
'''


class Solution(object):
    '''算法思路：

    同 I，dp[i][j] 表示前 i 个 house 如果第被喷上第 j 种颜色所需的最少的 cost

    Time: O(n*k^2)
    Space: O(n*k)
    '''
    def minCostII(self, costs):
        n, k = len(costs), len(costs[0]) if costs else 0

        dp = [[0] * k for _ in xrange(n + 1)]
        for i, row in enumerate(costs, 1):
            for j, cost in enumerate(row):
                dp[i][j] = min(dp[i - 1][:j] + dp[i - 1][j + 1:] or [0]) + cost

        return min(dp[n] or [0])


class Solution(object):
    '''算法思路：

    同上

    Time: O(n*k^2)
    Space: O(k)
    '''
    def minCostII(self, costs):
        n, k = len(costs), len(costs[0]) if costs else 0

        house = [0] * k
        for cost in costs:
            house = [
                min(house[:j] + house[j + 1:] or [0]) + cost[j]
                for j in xrange(k)
            ]
        return min(house or [0])


class Solution(object):
    '''算法思路：

    始终维护总体上最小和第二小两个数，层层遍历，计算每个 color 所能用的最小的 cost，
    用 min1 和 min2 两个 index 来记录最小和第二小的下标

    Time: O(nk)
    Space: O(1)
    '''
    def minCostII(self, costs):
        if not costs:
            return 0

        min1, min2 = -1, -1
        for i, row in enumerate(costs):
            originMin1, originMin2, min1, min2 = min1, min2, -1, -1

            for j, cost in enumerate(row):
                if j != originMin1:
                    row[j] += 0 if originMin1 < 0 else costs[i - 1][originMin1]
                else:
                    row[j] += 0 if originMin2 < 0 else costs[i - 1][originMin2]

                if min1 < 0 or row[j] < row[min1]:
                    min1, min2 = j, min1
                elif min2 < 0 or row[j] < row[min2]:
                    min2 = j

        return costs[-1][min1]


s = Solution()

print s.minCostII([8])
print s.minCostII([
    [8,16,12,18,9],
    [19,18,8,2,8],
    [8,5,5,13,4],
    [15,9,3,19,2],
    [8,7,1,8,17],
    [8,2,8,15,5],
    [8,17,1,15,3],
    [8,8,5,5,16],
    [2,2,18,2,9]
])
