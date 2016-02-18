# -*- coding: utf-8 -*-

'''
Walls and Gates
===============

You are given a m x n 2D grid initialized with these three possible values.

1. -1 - A wall or an obstacle.
2. 0 - A gate.
3. INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to
   represent INF as you may assume that the distance to a gate is less than
   2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible
to reach a gate, it should be filled with INF.

For example, given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

3  -1   0   1
2   2   1  -1
1  -1   2  -1
0  -1   3   4
'''


class Solution(object):
    '''算法思路：

    BFS
    '''
    def wallsAndGates(self, rooms):
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] != 0:
                    continue

                queue, distance = [(i, j)], 1
                while queue:
                    for _ in xrange(len(queue)):
                        x, y = queue.pop(0)
                        for row, col in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                            newX, newY = x + row, y + col

                            if (not (0 <= newX < m and 0 <= newY < n) or
                                    rooms[newX][newY] in [-1, 0] or
                                    distance >= rooms[newX][newY]):
                                continue

                            rooms[newX][newY] = distance
                            queue.append((newX, newY))
                    distance += 1


INF = float('inf')

s = Solution()
s.wallsAndGates([
    [INF,  -1,  0,  INF],
    [INF, INF, INF,  -1],
    [INF,  -1, INF,  -1],
    [0,  -1, INF, INF],
])
