# -*- coding: utf-8 -*-

'''
Dungeon Game
============

The demons had captured the princess (P) and imprisoned her in the bottom-right
corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid.
Our valiant knight (K) was initially positioned in the top-left room and must
fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at
any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative
integers) upon entering these rooms; other rooms are either empty (0's) or
contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to
move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is
able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be
at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)  -3    3
-5      -10   1
10      30    -5 (P)

Notes:

- The knight's health has no upper bound.
- Any room can contain threats or power-ups, even the first room the knight
  enters and the bottom-right room where the princess is imprisoned.
'''


class Solution(object):
    '''算法思路：

    DFS 搜索，可以想象成摩托车路上至少加多少油才能到达终点站

    设 added 为走过一站时至少需要加的油才能到达下一站，则：

    currentHealth + dungeon[i][j] + added >= 1，从而推出
    added >= max(1 - dungeon[i][j] - currentHealth), 每一站加的油总和即为初始生命

    Time: O(2^n)

    结果：TLE
    '''
    def dfs(self, dungeon, m, n, i, j, initHealth, currentHealth):
        if (i == m and j == n - 1 or
                i == m - 1 and j == n or initHealth > self.minHealth):
            self.minHealth = min(self.minHealth, initHealth)
            return

        if i == m or j == n:
            return

        added = max(1 - dungeon[i][j] - currentHealth, 0)
        initHealth += added
        currentHealth += added + dungeon[i][j]

        for x, y in ((0, 1), (1, 0)):
            self.dfs(dungeon, m, n, i + x, j + y, initHealth, currentHealth)

    def calculateMinimumHP(self, dungeon):
        self.minHealth = float('inf')
        self.dfs(dungeon, len(dungeon), len(dungeon[0]), 0, 0, 1, 1)
        return self.minHealth


class Solution(object):
    '''算法思路：

    dfs(i, j, health) 表示从 (i, j) 以 health 到 (m - 1, n - 1) 所需添加的最小血量，
    并用缓存把中间结果保存起来

    结果：TLE
    '''
    def cache(f):
        def method(obj, dungeon, m, n, i, j, health):
            key = '{}:{}:{}'.format(i, j, health)
            if key not in obj.cache:
                obj.cache[key] = f(obj, dungeon, m, n, i, j, health)
            return obj.cache[key]
        return method

    @cache
    def dfs(self, dungeon, m, n, i, j, health):
        if i >= m or j >= n:
            return float('inf')

        added = max(1 - health - dungeon[i][j], 0)
        if i == m - 1 and j == n - 1:
            return added

        health += added + dungeon[i][j]
        return min(self.dfs(
            dungeon, m, n, i + x, j + y, health) for x, y in ((0, 1), (1, 0))
        ) + added

    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])

        self.cache = {}
        return self.dfs(dungeon, m, n, 0, 0, 1) + 1


class Solution(object):
    '''算法思路：

    动态规划

    由于到最后一步的结果是固定的，即最小为 1，所以从后往前推导。从前往后推导由于从上一步
    到下一步所依赖的条件比价复杂，因此从后往前推导比较简单。

    有一个规则是，从确定以的一端开始。

    dp[i][j] 表示从 (i, j) 到 (m - 1, n - 1) 所需最小 health

    dp[i][j] = min(
        max(dp[i + 1][j] - dungeon[i][j], 1),
        max(dp[i][j + 1] - dungeon[i][j], 1)
    )

    结果：AC
    '''
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])

        dp = [[0] * n for _ in xrange(m)]
        dp[-1][-1] = max(1 - dungeon[-1][-1], 1)

        for i in xrange(m - 2, -1, -1):
            dp[i][-1] = max(dp[i + 1][-1] - dungeon[i][-1], 1)

        for j in xrange(n - 2, -1, -1):
            dp[-1][j] = max(dp[-1][j + 1] - dungeon[-1][j], 1)

        for i in xrange(m - 2, -1, -1):
            for j in xrange(n - 2, -1, -1):
                dp[i][j] = max(min(
                    dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)

        return dp[0][0]


class Solution(object):
    '''算法思路：

    同上，只不过简化了一下

    结果：AC
    '''
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [float('inf')] * (n - 1) + [1, float('inf')]

        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                dp[j] = max(min(dp[j + 1], dp[j]) - dungeon[i][j], 1)

        return dp[0]


s = Solution()
print s.calculateMinimumHP([[-3],[-7]])
